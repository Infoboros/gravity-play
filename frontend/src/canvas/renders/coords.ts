import {SVG} from "../types.ts";



export const transferCoordsToCanvas = (svg: SVG, x: number, y: number) => {
    const getNumberStyle = (style: string) => Number(
        svg
            .style(style)
            .replace("px", "")
    )
    return [
        x * getNumberStyle("width"),
        y * getNumberStyle("height")
    ]
}
