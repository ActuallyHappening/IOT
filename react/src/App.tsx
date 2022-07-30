import CredentialProvider from './CredentialProvider'
import Renderer from './Renderer'

const App = () => {
  return (
    <CredentialProvider>
      <Renderer />
    </CredentialProvider>
  )
}

export default App