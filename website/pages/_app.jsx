import '../styles/globals.css'
import EmailPopup from '../components/EmailPopup'

export default function App({ Component, pageProps }) {
  return (
    <>
      <Component {...pageProps} />
      <EmailPopup />
    </>
  )
}
