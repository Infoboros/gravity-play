

interface WindowParams {
    x: number
    y: number
    height: number
    width: number
}

export const getWindowParams = (): WindowParams => ({
    x: window.screenX,
    y: window.screenY,
    height: window.outerHeight,
    width: window.outerWidth
})
