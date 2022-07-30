import { createContext, useRef, useState } from "react"
import Aio, { fake_AIO, fake_AIO_gen, newAIO, T_aio } from "./lib/AIO"
import Renderer from "./Renderer"

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
export const Credentials = createContext<T_aio>(newAIO(_username, _key))

const Wrapper = ({children}:{
  children?: React.ReactNode
}) => {
  // const [username, setUsername] = useState<string|undefined>(_username)
  // const [key, setKey] = useState<string|undefined>(_key)
  const username = useRef(_username)
  const key = useRef(_key)

  let _show_dynamic_form = true
  if (username.current && key.current) {
    console.log("Username and key are set, hiding dynamic form: ", username, key)
    _show_dynamic_form = false
  } else {
    // console.log("Username and key are NOT set, SHOWING dynamic form",username, key)
  }
  
  // const [credentials, setCredentials] = useState<T_aio>("test 69")
  // const [credentials, setCredentials] = useState<T_aio>(fake_AIO_gen("[%%] STATE!!"))
  // const [credentials, setCredentials] = useState<T_aio>(_show_dynamic_form ? fake_AIO_gen("BBB n state") : newAIO(username.current, key.current))
  const [credentials, setCredentials] = useState<T_aio>(newAIO(username.current, key.current))

  return (
    // <Credentials.Provider value={fake_AIO_gen("Provided context GOOD!")}>
    <Credentials.Provider value={credentials}>
      <form
        style={{
          // display: _show_dynamic_form ? "block" : "none",
          left: "70%",
          top: "10%",
          position: "absolute",
        }}
        onSubmit={(e) => {
          e.preventDefault()
          console.log("Submitting form", username, key)
          if (username.current && key.current) {
            const _newAIOThingy = newAIO(username.current, key.current)
            console.warn("Setting new AIO thingy", _newAIOThingy)
            setCredentials(() => _newAIOThingy)
          } else {
            console.log("Username and key are not set, not updating credentials")
          }
        }}
      >
        <label>
          Enter AIO Username:
          <input type="text" name="username" onChange={(e) => {
            // setCredentials(e.target.value)
            username.current = e.target.value
          }}/>
        </label>
        <br/>
        <label>
          Enter AIO Key:
          <input type="text" name="key" onChange={(e) => {
            // setKey(e.target.value)
            key.current = e.target.value
          }}/>
        </label>
        {/* <br/>
        <label>AIO Username: {username.current}</label>
        <br/>
        <label>AIO Key: {key.current}</label>
        <br/>
        <label>Signed in: {String(!_show_dynamic_form)}</label>
        <br/> */}
        <input type="submit" value="Submit" />
      </form>
      {_show_dynamic_form ? null : children}
    </Credentials.Provider>
  )
}

export default Wrapper