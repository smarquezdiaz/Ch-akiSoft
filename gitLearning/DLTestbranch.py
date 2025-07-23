import requests

url = "https://www.metmuseum.org/events?type=music&_rsc=13byi"

payload = {}
headers = {
  'accept': '*/*',
  'accept-language': 'es-419,es;q=0.9',
  'baggage': 'sentry-environment=vercel-production,sentry-release=6bb4e3adc1939b3863e00863a4120196f9e2255f,sentry-public_key=fc26ffe1f7754e9aaa45cbb8fb82b860,sentry-trace_id=c33c73608159b3e4345d86ec204df52a,sentry-transaction=GET%20%2F%5Blocale%5D%2Fhubs%2F%5Bslug%5D,sentry-sampled=true,sentry-sample_rand=0.5933005232126529,sentry-sample_rate=1',
  'next-router-prefetch': '1',
  'next-router-state-tree': '%5B%22%22%2C%7B%22children%22%3A%5B%5B%22locale%22%2C%22en%22%2C%22d%22%5D%2C%7B%22children%22%3A%5B%22(navigation)%22%2C%7B%22children%22%3A%5B%22hubs%22%2C%7B%22children%22%3A%5B%5B%22slug%22%2C%22date-night-at-the-met%22%2C%22d%22%5D%2C%7B%22children%22%3A%5B%22__PAGE__%22%2C%7B%7D%2Cnull%2Cnull%5D%7D%2Cnull%2Cnull%5D%7D%2Cnull%2Cnull%5D%7D%2Cnull%2Cnull%5D%7D%2Cnull%2Cnull%5D%7D%2Cnull%2Cnull%2Ctrue%5D',
  'next-url': '/en/hubs/date-night-at-the-met',
  'priority': 'i',
  'referer': 'https://www.metmuseum.org/hubs/date-night-at-the-met',
  'rsc': '1',
  'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'sentry-trace': 'c33c73608159b3e4345d86ec204df52a-9bdcd48914ba7b43-1',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
  'Cookie': 'visid_incap_1662004=F6GBbEK2Sc++EYdAkTL0MewhgGgAAAAAQUIPAAAAAACXFYePaVKyV3ybK46nJQcF; incap_ses_1722_1662004=yTbaIkTNWV+H+TCDPcblF+0hgGgAAAAAcB4AnTnniWyS02eKkSm1Gg==; NEXT_LOCALE=en; _gcl_au=1.1.2033834480.1753227852; _gid=GA1.2.524718784.1753227852; _fbp=fb.1.1753227851978.754486219267583956; __spdt=0253a03048fa43d4a9175c63add7d6a4; _parsely_visitor={%22id%22:%22pid=f707c4a7-35f1-42a4-99d2-3158aa237e76%22%2C%22session_count%22:1%2C%22last_session_ts%22:1753227852204}; _tt_enable_cookie=1; _ttp=01K0T8BYGJH63785W68YS5NN1R_.tt.1; dtm_token=AQAIuopCPdRXnQF4_9kqAQBIaAABAQCNw1D1AQEBAJk1hPif; QuantumMetricUserID=d1c60e4f5d75c6db1ac59a84771b9f74; __qca=P1-fee8dc19-a28b-4343-9103-fd0abee3a6cd; visid_incap_1661922=jRQ0RQWtTaWqZ1u9JNOrzJ0igGgAAAAAQUIPAAAAAACqC/28VXlQd/oz9wcXhpoP; incap_ses_684_1661922=NEbtYoAsvCGY/S/Kqg5+CZ0igGgAAAAAmCozJcmEucndSKoEhjzWcA==; incap_ses_381_1661922=/yk1JWqWyUxPqaLUsJVJBakigGgAAAAA+zUunpnnEMxxXVbBnGlrTA==; _ga_Y0W8DGNBTB=GS2.1.s1753227851$o1$g1$t1753227946$j47$l0$h0; _ga=GA1.2.1298176010.1753227852; ttcsid=1753227852310::6EOPQEyWhbyLQ-QP_iY1.1.1753227946661; ttcsid_CA79G7RC77U7LMFB4PB0=1753227852309::sknAE1zkMvfXx_IR-7gz.1.1753227946890; ABTasty=uid=8w5ts3j0drxks4ch&fst=1753227852539&pst=-1&cst=1753227852539&ns=1&pvt=3&pvis=3&th=; QuantumMetricSessionID=39fbca3cdf320794adc7980a52ab01b0; incap_ses_1722_1662004=ZHWADK/aHRlr9TKDPcblFzUjgGgAAAAAru4ADlRPfBo+SaTiOpIf9w==; visid_incap_1662004=wZXoFaxIRw+X8vSGgDPE2zQjgGgAAAAAQUIPAAAAAADVmKDbGkTljb/XWLI/pG7c'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
