import {Planet, Solar, System} from "./index.ts";

function getRandomColor() {
    const letters = '0123456789ABCDEF';
    let color = '#';
    for (let i = 0; i < 6; i++) {
        color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
}

const range = (length: number) => Array.from({length})
const random = (min: number, max: number) => Math.floor(Math.random() * (max - min) + min)

const getRandomSolar = (): Solar => ({
    color: getRandomColor(),
    x: random(1, 10) / 10,
    y: random(1, 10) / 10,
    radius: random(1, 3) / 50,
})
const getRandomPlanet = (solar: Solar): Planet => ({
    color: getRandomColor(),

    x: solar.x,
    y: solar.y,

    rx: random(1, 5) / 10,
    ry: random(1, 5) / 10,

    rotate: random(1, 360),

    t: 0
})

const getRandomSystem = (): System => {
    const solar = getRandomSolar()
    return ({
        solar,
        planets: range(random(1, 5)).map(() => getRandomPlanet(solar))
    })
}

export const getRandomSystems = (): System[] => range(
    random(1, 4)
).map(getRandomSystem)
