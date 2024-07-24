import {HOST} from "./index.ts";


export const getClientSocket = (): WebSocket => {
    return new WebSocket(
        `ws://${HOST}/ws/client/`
    )
}
