import { Notify } from 'quasar'

export default function useUtility () {
  const notify = (message, color, duration, position, type) => {
    Notify.create({
      message,
      color,
      position,
      timeout: duration,
      type
    })
  }
  const errorNotif = (message) => notify(message, 'negative', '1000', 'top', 'negative')
  const successNotif = (message) => notify(message, 'positive', '1000', 'top', 'positive')
  const storage = (information) => {
    localStorage.setItem('email', information.email)
    localStorage.setItem('password', information.password)
  }
  return { notify, storage, errorNotif, successNotif }
}
