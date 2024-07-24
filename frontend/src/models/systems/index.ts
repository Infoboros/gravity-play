import {createEvent, createStore} from "effector";


export interface Planet {
    color: string

    x: number
    y: number

    rx: number
    ry: number

    rotate: number

    t: number
}

export interface Solar {
    color: string
    x: number
    y: number
    radius: number
}

export interface System{
    solar: Solar
    planets: Planet[]
}

export const $systems = createStore<System[]>([])

export const setState = createEvent<System[]>()

