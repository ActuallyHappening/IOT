import CredentialProvider from './components/credentials/CredentialProvider'
import Renderer from './Renderer'

const App = () => {
  return (
    <CredentialProvider>
      <Renderer />
    </CredentialProvider>
  )
}

export default App