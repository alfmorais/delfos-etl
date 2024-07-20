from sqlalchemy.orm import Session

from src.models.models import Data, Signal
from src.utils.session import SessionLocal
from sqlalchemy.exc import SQLAlchemyError


class LoadDataForDatabase:
    def __init__(
        self,
        initial_data: dict,
        signal_name: str,
        data: Data = Data,
        signal: Signal = Signal,
        session: Session = SessionLocal,
    ) -> None:
        self.initial_data = initial_data
        self.signal_name = signal_name
        self.data = data
        self.signal = signal
        self.session = session

    def create_signal(self) -> Signal:
        signal = self.signal(name=self.signal_name)

        with self.session() as session:
            session.add(signal)
            try:
                session.commit()
                session.refresh(signal)
            except Exception:
                session.rollback()
                raise SQLAlchemyError("Erro ao salvar signal no banco de dados")
            finally:
                session.close()

        return signal

    def create_batch_data(self) -> str:
        signal = self.create_signal()

        bulk_batch_data = list()

        for data in self.initial_data:
            new_data = self.data(
                signal_id=signal.id,
                timestamp=int(data["timestamp"]),
                value=data,
            )
            bulk_batch_data.append(new_data)

        with self.session() as session:
            session.bulk_save_objects(bulk_batch_data)

            try:
                session.commit()
            except Exception:
                session.rollback()

                raise SQLAlchemyError(
                    "Problema para salvar os registros no banco de dados",
                )
            finally:
                session.close()

        quantity = len(bulk_batch_data)
        return f"{quantity} objetos inserido com sucesso"
