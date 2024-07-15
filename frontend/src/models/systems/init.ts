import {$systems, nextState} from './index.ts'
import {System} from "./index";

// eslint-disable-next-line @typescript-eslint/no-unused-vars
const handleNextState = (prevState: System[], _: void) => prevState
    .map(
        ({planets, ...system}) => ({
            planets: planets.map(
                ({t, ...planet}) => ({
                    t: t + 0.01,
                    ...planet
                })
            ),
            ...system
        })
    )


$systems
    .on(nextState, handleNextState)
