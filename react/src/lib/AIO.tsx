import { defaultFrame } from "./ThermalCam"

export type T_Aio_definitiveConstructor = {
  username: string,
  key: string
}
export type T_Aio_fakeConstructor = T_Aio_definitiveConstructor & {
  // [P in keyof T_Aio_constructor]: T_Aio_constructor[P],
  isFake: boolean,
  data?: string,
}

export type T_Aio_constructor = T_Aio_definitiveConstructor | T_Aio_fakeConstructor
export type T_aio = (group: string, feed: string) => Promise<string>

const Aio = ({
  username,
  key,
  data,
  isFake,
}: T_Aio_constructor): T_aio => {
  if (isFake) {
    const _data = data ?? `{"stream": ${JSON.stringify(defaultFrame)}}`
    return async (group: string, feed: string) => {
      console.log("AIO api call fake (not signed in) for group:feed", group, feed)
      return _data
    }
  }
  return async (group: string, feed: string) => {
    const url = `https://io.adafruit.com/api/v2/${username}/feeds/${group}.${feed}/data?limit=1`
    const res = await fetch(url, {
      headers: {
        'X-AIO-Key': key,
      },
    })
    const data = await res.json()
    // console.log("_data", data)
    return data[0].value
  }
}

export const fake_AIO: T_aio = Aio({isFake: true})

export default Aio