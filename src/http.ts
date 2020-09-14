import axios from 'axios'
// promise-based http client https://github.com/axios/axios
// add the progress bar behavior to the http client
import Progress from './progress'

export const http = axios.create()

http.interceptors.request.use((config) => {
  Progress.start()

  return config
})

http.interceptors.response.use(
  (response) => {
    Progress.done()

    return response
  },
  (error) => {
    Progress.done()

    return Promise.reject(error)
  },
)

export default http
