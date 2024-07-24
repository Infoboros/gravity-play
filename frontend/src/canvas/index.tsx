import classes from "./index.module.css";
import {useEffect, useLayoutEffect} from "react";
import * as d3 from "d3"
import {useUnit} from "effector-react";
import {$systems, setState} from "../models/systems";
import {renderSystems} from "./renders/system.ts";
import {getClientSocket} from "../api/socket.ts";
import {getWindowParams} from "./renders/window.ts";

interface CanvasProps {
    id?: string
}

export default function Canvas(props: CanvasProps) {
    const {
        id = "canvas"
    } = props

    const systems = useUnit($systems)

    useEffect(
        () => {
            renderSystems(
                d3.select(`#${id}`),
                systems
            )
        }, [id, systems]
    )

    useLayoutEffect(() => {
        const socket = getClientSocket()
        socket.onmessage = ({data}) => {
            const message = JSON.parse(data).message
            setState(message)
        }
        const interval = setInterval(
            () => socket.send(JSON.stringify({message: getWindowParams()})),
            10
        )
        return () => {
            clearInterval(interval)
            socket.close()
        }
    }, []);

    return <svg
        id={id}
        className={classes.Canvas}
    />
}
