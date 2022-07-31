import CredentialProvider from './components/credentials/CredentialProvider'
import Renderer from './components/ThermalCam/ThermalRenderer'

const App = () => {
  return (
    <CredentialProvider>
      <Renderer />
    </CredentialProvider>
  )
}

export default App