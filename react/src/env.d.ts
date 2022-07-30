/// <reference types="vite/client" />

interface ImportMetaEnv {
  readonly VITE_ADAFRUIT_IO_USERNAME: string
  readonly VITE_ADAFRUIT_IO_KEY: string
  // more env variables...
}

interface ImportMeta {
  readonly env: ImportMetaEnv
}