import { createContext } from "react"

const _env_vars = import.meta.env
if (!_env_vars.VITE_ADAFRUIT_IO_USERNAME) {
  // throw new Error('AIO_USERNAME is not set')
  console.log("AIO_USERNAME is not found in env variables, requiring dynamic key")
}
const _username: undefined | string = _env_vars.VITE_ADAFRUIT_IO_USERNAME ?? undefined
if (!_env_vars.VITE_ADAFRUIT_IO_KEY) {
  // throw new Error('AIO_KEY is not set')
  console.log("AIO_KEY is not found in env variables, requiring dynamic key")
}
const _key: string | undefined = _env_vars.VITE_ADAFRUIT_IO_KEY ?? undefined

// export const Credentials = createContext<T_aio>("test NO WTF?")
// export const Credentials = createContext<T_aio>(fake_AIO_gen("BAD not updated context!:"))
const Credentials = createContext<{username: string, key: string}>({"username": _username, "key": _key})

export default Credentials