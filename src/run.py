import argparse

from src.etl.extract import DataExtractFromAPI
from src.etl.load import LoadDataForDatabase
from src.etl.transform import TransformData

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="ETL Delfos")
    parser.add_argument("start_time", type=int, help="Data Inicial")
    parser.add_argument("end_time", type=int, help="Data Final")
    parser.add_argument("signal", type=str, help="Signal")

    args = parser.parse_args()

    start_time = args.start_time
    end_time = args.end_time
    signal = args.signal

    total_items = []

    page = 1
    api = DataExtractFromAPI()
    status_code, response = api.read_data(start_time, end_time, page)
    total_items += response["items"]

    while response["page"] != response["pages"]:
        page += 1
        status_code, response = api.read_data(start_time, end_time, page)
        total_items += response["items"]

    transform_data = TransformData(total_items)
    initial_data = transform_data.generate_sanitize_data()

    load_data = LoadDataForDatabase(initial_data, signal)
    final_response = load_data.create_batch_data()
    print(final_response)
