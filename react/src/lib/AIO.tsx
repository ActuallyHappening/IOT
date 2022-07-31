import { createContext } from "react"
import { defaultFrame } from "../components/ThermalCam/ThermalCam"

export type T_Aio_definitiveConstructor = {
  username: string,
  key: string
}
export type T_Aio_fakeConstructor = T_Aio_definitiveConstructor & {
  // [P in keyof T_Aio_constructor]: T_Aio_constructor[P],
  isFake: boolean,
  data?: string,
  msg?: string,
}

export type T_Aio_constructor = T_Aio_definitiveConstructor | T_Aio_fakeConstructor
export type T_aio = (group: string, feed: string) => Promise<string>

const Aio = ({
  username,
  key,
}: T_Aio_constructor): T_aio => {
  console.log("constructing Aio", username, key)
  const r = async (group: string, feed: string) => {
    const url = `https://io.adafruit.com/api/v2/${username}/feeds/${group}.${feed}/data?limit=1`
    // console.warn("url is", url)
    const res = await fetch(url, {
      headers: {
        'X-AIO-Key': key,
      },
    })
    const data = await res.json()
    // console.log("_data", data)
    return data[0].value
  }
  return r
}

export const newAIO = (username: string, key: string): T_aio => Aio({username, key})

export const fake_AIO: T_aio = async (f: string, g: string) => {
  console.log("fake_AIO", f, g)
  return JSON.stringify({"stream": defaultFrame})
} 
export const fake_AIO_gen = (message: string): T_aio => {
  return (g, f) => {
    console.log("fake_AIO_gen", message)
    return fake_AIO(g, f)
  }
}

export const aio = createContext(fake_AIO_gen("aio not signed in :)"))

export default Aio