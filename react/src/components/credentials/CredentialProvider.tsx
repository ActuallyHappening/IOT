import { useContext, useRef, useState } from "react"
import Aio, { aio, fake_AIO, fake_AIO_gen, newAIO, T_aio } from "../../lib/AIO"
import Credentials from "./Credentials"

const Wrapper = ({children}:{
  children?: React.ReactNode
}) => {
  // Context gives env var versions of username and key
  const {username: _username, key: _key} = useContext(Credentials)
  const [username, setUsername] = useState(_username)
  const [key, setKey] = useState(_key)

  let require_form = true
  if (username && key) {
    console.log("Username and key are set, hiding dynamic form: ", username, key)
    require_form = false
  } else {
    console.log("Username and key are NOT set, SHOWING dynamic form", username, key)
  }

  return (
    <aio.Provider value={newAIO(username, key)}>
      {children}
      <form
        style={{
          left: "70%",
          top: "10%",
          position: "absolute",
        }}
      >
        <label>
          Enter AIO Username:
          <input type="text" name="username" onChange={(e) => setUsername(e.target.value)}/>
        </label>
        <br/>
        <label>
          Enter AIO Key:
          <input type="text" name="key" onChange={(e) => setKey(e.target.value)}/>
        </label>
        <br/>
        <label>AIO Username: {username}</label>
        <br/>
        <label>AIO Key: {key}</label>
        <br/>
        <label>Signed in: {String(!require_form)}</label>
        <br/>
        {/* <input type="submit" value="Sign In" /> */}
      </form>
    </aio.Provider>
  )
}

export default Wrapper