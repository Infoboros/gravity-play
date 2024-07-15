import {System} from "../../models/systems";
import {SVG} from "../types.ts";
import {renderSolar} from "./solar.ts";
import {renderPlanet} from "./planet.ts";

const clearCanvas = (svg: SVG) => svg.selectAll("*").remove()

export const renderSystem = (svg: SVG, system: System) => {
    renderSolar(svg, system.solar)
    system
        .planets
        .forEach(
            planet =>
                renderPlanet(svg, planet)
        )
}


export const renderSystems = (svg: SVG, systems: System[]) => {
    clearCanvas(svg)
    systems
        .forEach(
            system => {
                renderSystem(svg, system)
            }
        )
}

