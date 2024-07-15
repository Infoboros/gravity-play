import {transferCoordsToCanvas} from "./coords.ts";
import {Solar} from "../../models/systems";
import {SVG} from "../types.ts";

export const renderSolar = (svg: SVG, solar: Solar) => {
    const [cx, cy] = transferCoordsToCanvas(
        svg,
        solar.x,
        solar.y
    )
    const [rx, ry] = transferCoordsToCanvas(
        svg,
        solar.radius,
        solar.radius
    )

    svg
        .append("circle")
        .attr("cx", cx)
        .attr("cy", cy)
        .attr("r", Math.min(rx, ry))
        .attr("fill", solar.color)
}
