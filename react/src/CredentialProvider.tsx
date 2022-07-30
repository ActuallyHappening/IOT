import { createContext } from "react"
import App from "./Renderer"

const _env_vars = import.meta.env
if (!_env_vars.VITE_ADAFRUIT_IO_USERNAME) {
  // throw new Error('AIO_USERNAME is not set')
  console.log("AIO_USERNAME is not set, requiring dynamic key")
}
const _username: boolean | string = _env_vars.VITE_ADAFRUIT_IO_USERNAME ?? undefined
if (!_env_vars.VITE_ADAFRUIT_IO_KEY) {
  // throw new Error('AIO_KEY is not set')
  console.log("AIO_KEY is not set, requiring dynamic key")
}
const _key = _env_vars.VITE_ADAFRUIT_IO_KEY ?? undefined

export const Credentials = createContext<

const Wrapper = () => {
  const credentials = 
  const [_username, _setUsername] = useState<string>(username ?? "Not set")
  const [_key, _setKey] = useState<string>(username ?? "Not set")
  let _show_dynamic_form = false
  let aio = async (g:string,f:string): Promise<string> => {
    console.log("AIO api call not signed in for group:feed", g, f)
    return JSON.stringify({"stream": _defaultFrame})
  }
  if (!username || !key) {
    _show_dynamic_form = true
  } else {
    aio = Aio(username, key)
  }
  return (
    <Credentials.Provider value={{username: _username, key: _key}}>
      <form
        style={{
          display: _show_dynamic_form ? "block" : "none",
          left: "80%",
          top: "10%",
          position: "absolute",
        }}
        onSubmit={(e) => {
          e.preventDefault()
          setContext({ username: _username, key: _key })
        }}
      >
        <label>
          Enter AIO Username:
          <input type="text" name="username" />
        </label>
        <label>
          Enter AIO Key:
          <input type="text" name="key" />
        </label>
        <input type="submit" value="Submit" />
      </form>
      <App />
    </Credentials.Provider>
  )
}

export default Wrapper