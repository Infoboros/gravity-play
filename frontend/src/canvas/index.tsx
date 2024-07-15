import classes from "./index.module.css";
import {useEffect} from "react";
import * as d3 from "d3"
import {useUnit} from "effector-react";
import {$systems, nextState} from "../models/systems";
import {renderSystems} from "./renders/system.ts";

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

    useEffect(() => {
        const interval = setInterval(
            () => nextState(), 10
        )
        return () => clearInterval(interval)
    }, []);


    return <svg
        id={id}
        className={classes.Canvas}
    />
}
