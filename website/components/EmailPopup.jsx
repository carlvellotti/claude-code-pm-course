import { useEffect, useState, useRef } from 'react'

// Brand colors
const colors = {
  maple: '#e63f02',
  mapleDark: '#b43200',
  mapleWash: '#fff0eb',
  butter: '#f4d35e',
  gold: '#fcc403',
  ink: '#1a1612',
  stone700: '#5c5248',
  stone600: '#7a6e62',
  stone400: '#b8a99a',
  stone200: '#e8e0d6',
  stone50: '#faf8f5',
  success: '#2d8a4e',
}

const CheckIcon = () => (
  <svg style={{ width: 14, height: 14 }} fill="currentColor" viewBox="0 0 20 20">
    <path fillRule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clipRule="evenodd" />
  </svg>
)

const Spinner = () => (
  <svg style={{ width: 16, height: 16, animation: 'spin 1s linear infinite' }} viewBox="0 0 24 24">
    <circle style={{ opacity: 0.25 }} cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4" fill="none" />
    <path style={{ opacity: 0.75 }} fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z" />
  </svg>
)

const TrustSignal = ({ children }) => (
  <span className="trust-signal">
    <span className="trust-check"><CheckIcon /></span>
    {children}
  </span>
)

// Analytics helper
const trackEvent = (eventName, params = {}) => {
  if (typeof window !== 'undefined' && window.gtag) {
    window.gtag('event', eventName, params)
  }
}

export default function EmailPopup() {
  const [isVisible, setIsVisible] = useState(false)
  const [email, setEmail] = useState('')
  const [status, setStatus] = useState('idle') // idle（空闲）, loading（加载中）, success（成功）, error（错误）
  const [errorMessage, setErrorMessage] = useState('')
  const inputRef = useRef(null)

  useEffect(() => {
    // 检查用户是否已经看过弹窗
    const hasSeenPopup = localStorage.getItem('fspm-popup-seen')
    if (hasSeenPopup) return

    // 10秒后显示弹窗
    const timer = setTimeout(() => {
      setIsVisible(true)
      trackEvent('popup_shown', { popup_type: 'email_signup', source: 'ccforpms' })
    }, 10000)

    return () => clearTimeout(timer)
  }, [])

  useEffect(() => {
    if (isVisible && inputRef.current) {
      inputRef.current.focus()
    }
  }, [isVisible])

  const handleClose = () => {
    setIsVisible(false)
    localStorage.setItem('fspm-popup-seen', 'true')
    trackEvent('popup_closed', { popup_type: 'email_signup', source: 'ccforpms' })
  }

  const handleSubmit = async (e) => {
    e.preventDefault()
    if (!email) return

    setStatus('loading')
    setErrorMessage('')

    try {
      // Use fullstackpm.com API (same Beehiiv publication)
      const response = await fetch('https://fullstackpm.com/api/subscribe', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          email,
          source: 'ccforpms-popup',
          utm_source: 'ccforpms',
          utm_medium: 'popup',
          utm_campaign: 'course-popup',
          landing_page: window.location.pathname,
          referrer: document.referrer || 'direct',
        }),
      })

      const data = await response.json()

      if (response.ok && data.success) {
        setStatus('success')
        localStorage.setItem('fspm-popup-seen', 'true')
        trackEvent('popup_submitted', { popup_type: 'email_signup', source: 'ccforpms' })
        setTimeout(() => {
          setIsVisible(false)
        }, 2500)
      } else {
        setStatus('error')
        setErrorMessage(data.error || 'Something went wrong. Please try again.')
      }
    } catch (err) {
      setStatus('error')
      setErrorMessage('Network error. Please try again.')
    }
  }

  if (!isVisible) return null

  return (
    <>
      {/* 遮罩层 */}
      <div className="popup-overlay" onClick={handleClose} />

      {/* 弹窗 */}
      <div className="popup-container">
        {/* 关闭按钮 */}
        <button className="popup-close" onClick={handleClose} aria-label="关闭弹窗">
          ×
        </button>

        <div className="popup-gradient-edge" />

        <div className="popup-context-bar">
          Claude Code for PMs 隶属于 <a href="https://fullstackpm.com" target="_blank" rel="noopener noreferrer">The Full Stack PM</a>
        </div>

        {status === 'success' ? (
          <div className="popup-content">
            <div className="popup-success">
              <span className="popup-success-icon">🥞</span>
              <h3>你已加入 Stack！</h3>
              <p>请查看收件箱，查收来自 Carl 的欢迎邮件。</p>
            </div>
          </div>
        ) : (
          <div className="popup-content">
            <div className="popup-inner">
              {/* 左侧 - 价值主张 */}
              <div className="popup-left">
                <div className="popup-header">
                  <span className="popup-emoji">🥞</span>
                  <div>
                    <h3>加入 Stack</h3>
                    <p className="popup-subhead">
                      加入 <strong>12,000+</strong> 位使用 AI 构建产品的产品经理
                    </p>
                  </div>
                </div>
                <p className="popup-description">
                  获取每周见解，学习如何使用 Claude Code 和 Cursor 等 AI 工具构建原型、自动化工作流等。
                </p>
              </div>

              {/* 右侧 - 表单 */}
              <div className="popup-right">
                <form onSubmit={handleSubmit} className="popup-form">
                  <input
                    ref={inputRef}
                    type="email"
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                    placeholder="you@company.com"
                    required
                    disabled={status === 'loading'}
                  />
                  <button type="submit" disabled={status === 'loading'}>
                    {status === 'loading' ? (
                      <><Spinner /> 加入中...</>
                    ) : (
                      '加入 Stack'
                    )}
                  </button>
                </form>
                {status === 'error' && (
                  <p className="popup-error">{errorMessage}</p>
                )}
                <div className="popup-trust">
                  <TrustSignal>拒绝垃圾邮件</TrustSignal>
                  <TrustSignal>随时退订</TrustSignal>
                  <TrustSignal>每周一更</TrustSignal>
                </div>
              </div>
            </div>
          </div>
        )}

        <div className="popup-footer">
          由 <a href="https://www.linkedin.com/in/carlvellotti/" target="_blank" rel="noopener noreferrer">Carl Vellotti</a> 用 💛 和 🥞 制作
        </div>
      </div>

      <style jsx global>{`
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700&display=swap');

        @keyframes spin {
          from { transform: rotate(0deg); }
          to { transform: rotate(360deg); }
        }

        .trust-signal {
          display: inline-flex;
          align-items: center;
          gap: 6px;
        }
        .trust-check {
          width: 16px;
          height: 16px;
          border-radius: 50%;
          background: ${colors.success}15;
          color: ${colors.success};
          display: inline-flex;
          align-items: center;
          justify-content: center;
        }
      `}</style>

      <style jsx>{`
        .popup-overlay {
          position: fixed;
          inset: 0;
          background: rgba(0, 0, 0, 0.6);
          z-index: 9998;
          animation: fadeIn 0.3s ease;
        }

        .popup-container {
          position: fixed;
          bottom: 0;
          left: 0;
          right: 0;
          z-index: 9999;
          font-family: 'Outfit', system-ui, sans-serif;
          animation: slideUp 0.4s cubic-bezier(0.16, 1, 0.3, 1) both;
        }

        .popup-close {
          position: absolute;
          top: 8px;
          right: 16px;
          width: 28px;
          height: 28px;
          display: flex;
          align-items: center;
          justify-content: center;
          background: white;
          border: 1px solid ${colors.stone200};
          border-radius: 50%;
          font-size: 18px;
          line-height: 1;
          color: ${colors.stone600};
          cursor: pointer;
          transition: all 0.2s;
          z-index: 10;
        }
        .popup-close:hover {
          background: ${colors.stone50};
          color: ${colors.ink};
        }

        .popup-gradient-edge {
          height: 4px;
          background: linear-gradient(90deg, ${colors.butter}, ${colors.maple}, ${colors.butter});
        }

        .popup-context-bar {
          padding: 10px 24px;
          background: ${colors.stone50};
          border-bottom: 1px solid ${colors.stone200};
          font-size: 13px;
          color: ${colors.stone600};
          text-align: center;
        }
        .popup-context-bar a {
          color: ${colors.maple};
          text-decoration: none;
          font-weight: 500;
        }
        .popup-context-bar a:hover {
          text-decoration: underline;
        }

        .popup-footer {
          padding: 12px 24px;
          background: ${colors.stone50};
          border-top: 1px solid ${colors.stone200};
          font-size: 13px;
          color: ${colors.stone600};
          text-align: center;
        }
        .popup-footer a {
          color: ${colors.maple};
          text-decoration: none;
          font-weight: 500;
        }
        .popup-footer a:hover {
          text-decoration: underline;
        }

        .popup-content {
          background: linear-gradient(to bottom right, #fffcf5, white);
          padding: 20px 24px 16px;
        }

        .popup-inner {
          display: flex;
          flex-direction: column;
          gap: 24px;
          max-width: 900px;
          margin: 0 auto;
        }

        .popup-left {
          flex: 1;
        }

        .popup-header {
          display: flex;
          align-items: center;
          gap: 16px;
        }

        .popup-emoji {
          font-size: 40px;
          animation: float 4s ease-in-out infinite;
        }

        .popup-header h3 {
          font-size: 22px;
          font-weight: 700;
          color: ${colors.ink};
          margin: 0;
          font-family: 'Outfit', system-ui, sans-serif;
        }

        .popup-subhead {
          font-size: 14px;
          color: ${colors.stone600};
          margin: 4px 0 0;
        }
        .popup-subhead strong {
          color: ${colors.ink};
        }

        .popup-description {
          margin: 16px 0 0;
          color: ${colors.stone700};
          line-height: 1.6;
        }

        .popup-right {
          flex-shrink: 0;
        }

        .popup-form {
          display: flex;
          flex-direction: column;
          gap: 12px;
        }

        .popup-form input {
          flex: 1;
          padding: 14px 18px;
          font-size: 15px;
          font-family: inherit;
          background: white;
          border: 2px solid ${colors.stone200};
          border-radius: 12px;
          outline: none;
          transition: all 0.2s;
          color: ${colors.ink};
        }
        .popup-form input::placeholder {
          color: ${colors.stone400};
        }
        .popup-form input:focus {
          border-color: ${colors.maple};
          box-shadow: 0 0 0 4px ${colors.mapleWash};
        }

        .popup-form button {
          padding: 14px 24px;
          font-size: 15px;
          font-weight: 600;
          font-family: inherit;
          color: white;
          background: ${colors.maple};
          border: none;
          border-radius: 12px;
          cursor: pointer;
          white-space: nowrap;
          display: inline-flex;
          align-items: center;
          justify-content: center;
          gap: 8px;
          transition: all 0.25s cubic-bezier(0.25, 1, 0.5, 1);
          box-shadow: 0 4px 14px rgba(230, 63, 2, 0.25);
        }
        .popup-form button:hover {
          background: ${colors.mapleDark};
          transform: translateY(-2px);
          box-shadow: 0 8px 24px rgba(230, 63, 2, 0.35);
        }
        .popup-form button:disabled {
          opacity: 0.7;
          cursor: not-allowed;
          transform: none;
        }

        .popup-error {
          margin: 12px 0 0;
          font-size: 14px;
          color: #c41e1e;
          text-align: center;
        }

        .popup-trust {
          display: flex;
          flex-wrap: wrap;
          justify-content: center;
          gap: 16px;
          margin-top: 12px;
          font-size: 13px;
          color: ${colors.stone600};
        }

        .popup-success {
          text-align: center;
          padding: 20px 0;
        }
        .popup-success-icon {
          font-size: 48px;
          display: block;
          margin-bottom: 16px;
          animation: float 3s ease-in-out infinite;
        }
        .popup-success h3 {
          font-size: 24px;
          font-weight: 700;
          color: ${colors.ink};
          margin: 0 0 8px;
          font-family: 'Outfit', system-ui, sans-serif;
        }
        .popup-success p {
          color: ${colors.stone600};
          margin: 0;
        }

        @media (min-width: 640px) {
          .popup-content {
            padding: 40px;
          }
          .popup-inner {
            flex-direction: row;
            align-items: center;
          }
          .popup-right {
            width: 340px;
          }
          .popup-form {
            flex-direction: row;
          }
          .popup-trust {
            justify-content: flex-start;
          }
        }

        @keyframes fadeIn {
          from { opacity: 0; }
          to { opacity: 1; }
        }

        @keyframes slideUp {
          from { transform: translateY(100%); opacity: 0; }
          to { transform: translateY(0); opacity: 1; }
        }

        @keyframes float {
          0%, 100% { transform: translateY(0); }
          50% { transform: translateY(-8px); }
        }
      `}</style>
    </>
  )
}
