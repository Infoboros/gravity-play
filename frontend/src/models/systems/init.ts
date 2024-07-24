import {$systems, setState} from './index.ts'
import {System} from "./index";

// eslint-disable-next-line @typescript-eslint/no-unused-vars
const handleSetState = (_: System[], newState: System[]) => newState


$systems
    .on(setState, handleSetState)
