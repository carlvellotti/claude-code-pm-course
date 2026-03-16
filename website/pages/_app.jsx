import '../styles/globals.css'
import EmailPopup from '../components/EmailPopup'
import DownloadGate from '../components/DownloadGate'

export default function App({ Component, pageProps }) {
  return (
    <>
      <Component {...pageProps} />
      <EmailPopup />
      <DownloadGate />
    </>
  )
}
