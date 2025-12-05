import { useEffect, useState } from 'react'

export default function EmailPopup() {
  const [isVisible, setIsVisible] = useState(false)
  const [isLoaded, setIsLoaded] = useState(false)
  const [iframeUrl, setIframeUrl] = useState('')

  useEffect(() => {
    // Check if user has already seen the popup
    const hasSeenPopup = localStorage.getItem('beehiiv-popup-seen')

    if (hasSeenPopup) {
      return // Don't show if already seen
    }

    // Build iframe URL with attribution data
    const baseUrl = 'https://subscribe-forms.beehiiv.com/792a1ed7-1dd0-4ffa-af11-b407d7efac14'
    const params = new URLSearchParams({
      utm_source: 'ccforpms',
      utm_medium: 'popup',
      utm_campaign: 'course-popup',
      ref_url: window.location.href,
      referrer: document.referrer || 'direct'
    })
    setIframeUrl(`${baseUrl}?${params.toString()}`)

    // Show popup after 10 seconds
    const timer = setTimeout(() => {
      setIsVisible(true)
    }, 10000)

    return () => clearTimeout(timer)
  }, [])

  useEffect(() => {
    // Load Beehiiv script
    if (isVisible && !isLoaded) {
      const script = document.createElement('script')
      script.src = 'https://subscribe-forms.beehiiv.com/embed.js'
      script.async = true
      document.body.appendChild(script)
      setIsLoaded(true)
    }
  }, [isVisible, isLoaded])

  const handleClose = () => {
    setIsVisible(false)
    localStorage.setItem('beehiiv-popup-seen', 'true')
  }

  if (!isVisible) return null

  return (
    <>
      {/* Overlay */}
      <div
        className="popup-overlay"
        onClick={handleClose}
      />

      {/* Popup Container */}
      <div className="popup-container">
        {/* Close button */}
        <button
          className="popup-close"
          onClick={handleClose}
          aria-label="Close popup"
        >
          ×
        </button>

        {/* Beehiiv Form */}
        <iframe
          src={iframeUrl}
          className="beehiiv-embed"
          data-test-id="beehiiv-embed"
          frameBorder="0"
          scrolling="auto"
          style={{
            width: '100%',
            height: '190px',
            margin: 0,
            borderRadius: '5px',
            backgroundColor: 'transparent',
            border: 'none',
            maxWidth: '100%'
          }}
        />
      </div>

      {/* Inline Styles */}
      <style jsx>{`
        .popup-overlay {
          position: fixed;
          top: 0;
          left: 0;
          right: 0;
          bottom: 0;
          background: rgba(0, 0, 0, 0.7);
          z-index: 9998;
          animation: fadeIn 0.3s ease-in-out;
        }

        .popup-container {
          position: fixed;
          top: 50%;
          left: 50%;
          transform: translate(-50%, -50%);
          background: transparent;
          padding: 0;
          border-radius: 12px;
          max-width: 500px;
          width: 90%;
          z-index: 9999;
          animation: slideUp 0.3s ease-in-out;
        }

        .popup-close {
          position: absolute;
          top: 0.5rem;
          right: 0.5rem;
          background: transparent;
          border: none;
          color: #888;
          font-size: 2rem;
          cursor: pointer;
          width: 32px;
          height: 32px;
          display: flex;
          align-items: center;
          justify-content: center;
          transition: color 0.2s;
          z-index: 10;
        }

        .popup-close:hover {
          color: #fff;
        }

        .popup-content {
          color: #fff;
        }

        @keyframes fadeIn {
          from {
            opacity: 0;
          }
          to {
            opacity: 1;
          }
        }

        @keyframes slideUp {
          from {
            opacity: 0;
            transform: translate(-50%, -40%);
          }
          to {
            opacity: 1;
            transform: translate(-50%, -50%);
          }
        }

        @media (max-width: 640px) {
          .popup-container {
            width: 95%;
          }

          .beehiiv-embed {
            height: 350px !important;
          }
        }
      `}</style>
    </>
  )
}
