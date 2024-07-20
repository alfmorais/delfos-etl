import httpx


class DataExtractFromAPI:
    def __init__(self) -> None:
        self.requester = httpx
        self.base_url = self.__base_url

    @property
    def __base_url(self) -> str:
        return "http://localhost:8000"

    def read_data_from_api_url(
        self,
        start_time: int,
        end_time: int,
        page: int = 1,
    ) -> str:
        size = 100
        columns = "timestamp,wind_speed,power"

        endpoint = "/v1/data"
        params = f"?start_time={start_time}&end_time={end_time}&columns={columns}&page={page}&size={size}"  # noqa E501
        params_complete = params.format(
            start_time=start_time,
            end_time=end_time,
            columns=columns,
            page=page,
            size=size,
        )

        complete_url = "{base_url}{endpoint}{params_complete}".format(
            base_url=self.base_url,
            endpoint=endpoint,
            params_complete=params_complete,
        )
        return complete_url

    def read_data(
        self,
        start_time: int,
        end_time: int,
        page: int = 1,
    ) -> tuple:
        url = self.read_data_from_api_url(start_time, end_time, page)
        response = self.requester.get(url=url)
        return response.status_code, response.json()
