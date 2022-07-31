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
    // <Credentials.Provider value={fake_AIO_gen("Provided context GOOD!")}>
    <aio.Provider value={newAIO(username, key)}>
      {/* {require_form ? null : children} */}
      {children}
      <form
        style={{
          // display: _show_dynamic_form ? "block" : "none",
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
        {/* <br/>
        <label>AIO Username: {username.current}</label>
        <br/>
        <label>AIO Key: {key.current}</label>
        <br/>
        <label>Signed in: {String(!_show_dynamic_form)}</label> */}
        <br/>
        <input type="submit" value="Sign In" />
      </form>
    </aio.Provider>
  )
}

export default Wrapper