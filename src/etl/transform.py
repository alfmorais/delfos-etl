import pandas as pd
import math


class TransformData:
    def __init__(self, data: list) -> None:
        self.data = data
        self.agg_functions = {
            "wind_speed": ["mean", "min", "max", "std"],
            "power": ["mean", "min", "max", "std"],
        }

    def generate_sanitize_data(self) -> list:
        dataframe = pd.DataFrame(self.data)
        dataframe["wind_speed"] = pd.to_numeric(dataframe["wind_speed"])
        dataframe["power"] = pd.to_numeric(dataframe["power"])
        dataframe["timestamp"] = pd.to_datetime(
            dataframe["timestamp"],
            unit="s",
        )
        dataframe.set_index("timestamp", inplace=True)
        response = dataframe.resample("10min").agg(self.agg_functions)
        response.columns = ["_".join(col) for col in response.columns]
        response = response.round(2)
        response = response.reset_index()
        response["timestamp"] = response["timestamp"].astype(int) / 10**9
        final_response = response.to_dict(orient="records")
        return self.cleaned_data(final_response)

    def cleaned_data(self, response: list) -> list:
        sanitize_data = list()

        for data in response:
            cleaned_data = {}
            for key, value in data.items():
                if isinstance(value, float) and (
                    math.isnan(value) or value == float("nan")
                ):
                    cleaned_data[key] = None
                else:
                    cleaned_data[key] = value
            sanitize_data.append(cleaned_data)

        return sanitize_data
