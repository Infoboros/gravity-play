import {SVG} from "../types.ts";
import {Planet} from "../../models/systems";
import {transferCoordsToCanvas} from "./coords.ts";


export const renderPlanet = (svg: SVG, planet: Planet) => {
    const [cx, cy] = transferCoordsToCanvas(
        svg,
        planet.x,
        planet.y
    )
    const [rx, ry] = transferCoordsToCanvas(
        svg,
        planet.rx,
        planet.ry
    )

    const px = planet.rx * Math.cos(planet.t) + planet.x
    const py = planet.ry * Math.sin(planet.t) + planet.y
    const [cpx, cpy] = transferCoordsToCanvas(
        svg,
        px,
        py
    )

    const rotate = `rotate(${planet.rotate} ${cx} ${cy})`
    svg
        .append("ellipse")
        .attr("cx", cx)
        .attr("cy", cy)
        .attr("rx", rx)
        .attr("ry", ry)
        .attr("fill", "none")
        .attr("stroke", planet.color)
        .attr("stroke-width", "1px")
        .attr("transform", rotate)

    svg
        .append("circle")
        .attr("cx", cpx)
        .attr("cy", cpy)
        .attr("r", 10)
        .attr("fill", planet.color)
        .attr("transform", rotate)

}
