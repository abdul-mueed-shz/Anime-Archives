import { Notify } from 'quasar'

const notify = (message, color, duration, position) => {
  Notify.create({
    message,
    color,
    position,
    timeout: duration
  })
}
const storage = (information) => {
  localStorage.setItem('email', information.email)
  localStorage.setItem('password', information.password)
}
export default {
  notify,
  storage
}
