from core.controllers.system import SystemController, SystemDTO
from core.models import Client, Window


class ClientController:
    class SessionNotFound(Exception):
        pass

    def __init__(self, client: Client):
        self.client = client
        self.window = None
        self.system_controller = None

    @staticmethod
    async def get_or_create(session_id: str) -> 'ClientController':
        client, _ = await Client.objects.aget_or_create(
            session_id=session_id
        )

        return ClientController(client)

    @staticmethod
    async def get_by_headers(headers: (str, str)) -> 'ClientController':
        for key, value in headers:
            if key == b"cookie":
                session_id = list(filter(lambda x: "sessionid" in x, str(value).split('; ')))
                if session_id:
                    prepared_session_id = (
                        session_id[0]
                        .replace("sessionid=", "")
                        .replace("'", "")
                    )
                    return await ClientController.get_or_create(prepared_session_id)
        raise ClientController.SessionNotFound

    async def update_window(
            self,
            x: float,
            y: float,
            height: float,
            width: float
    ):
        if self.window is None:
            self.window = await Window.objects.acreate(
                client=self.client,
                x=x,
                y=y,
                height=height,
                width=width
            )
            self.system_controller = await SystemController.create_random_system(self.window)
        else:
            self.window.x = x
            self.window.y = y
            self.window.height = height
            self.window.width = width
            await self.window.asave()

    async def delete_window(self):
        if self.window:
            await self.window.adelete()

    async def get_render_info(self) -> [SystemDTO]:
        system_controllers = [self.system_controller]

        for system_controller in system_controllers:
            yield system_controller.get_render_info()
            await system_controller.next_state()

