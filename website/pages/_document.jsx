import { Html, Head, Main, NextScript } from 'next/document'

const META_PIXEL_ID = process.env.NEXT_PUBLIC_META_PIXEL_ID
const LINKEDIN_PARTNER_ID = process.env.NEXT_PUBLIC_LINKEDIN_PARTNER_ID

export default function Document() {
  return (
    <Html lang="en">
      <Head>
        {/* Meta Pixel */}
        {META_PIXEL_ID && (
          <>
            <script
              dangerouslySetInnerHTML={{
                __html: `!function(f,b,e,v,n,t,s){if(f.fbq)return;n=f.fbq=function(){n.callMethod?n.callMethod.apply(n,arguments):n.queue.push(arguments)};if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';n.queue=[];t=b.createElement(e);t.async=!0;t.src=v;s=b.getElementsByTagName(e)[0];s.parentNode.insertBefore(t,s)}(window,document,'script','https://connect.facebook.net/en_US/fbevents.js');fbq('init','${META_PIXEL_ID}');fbq('track','PageView');`,
              }}
            />
            <noscript>
              <img
                height="1"
                width="1"
                style={{ display: 'none' }}
                src={`https://www.facebook.com/tr?id=${META_PIXEL_ID}&ev=PageView&noscript=1`}
                alt=""
              />
            </noscript>
          </>
        )}

        {/* LinkedIn Insight Tag */}
        {LINKEDIN_PARTNER_ID && (
          <>
            <script
              dangerouslySetInnerHTML={{
                __html: `_linkedin_partner_id="${LINKEDIN_PARTNER_ID}";window._linkedin_data_partner_ids=window._linkedin_data_partner_ids||[];window._linkedin_data_partner_ids.push(_linkedin_partner_id);`,
              }}
            />
            <script
              async
              src="https://snap.licdn.com/li.lms-analytics/insight.min.js"
            />
            <noscript>
              <img
                height="1"
                width="1"
                style={{ display: 'none' }}
                alt=""
                src={`https://px.ads.linkedin.com/collect/?pid=${LINKEDIN_PARTNER_ID}&fmt=gif`}
              />
            </noscript>
          </>
        )}
      </Head>
      <body>
        <Main />
        <NextScript />
      </body>
    </Html>
  )
}
