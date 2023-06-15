import { computed } from 'vue'
import { useStore } from 'vuex'
import { useQuasar } from 'quasar'

export default function useComputes () {
  const $q = useQuasar()
  const store = useStore()
  const MAP = computed(() => store.getters['translations/getMap'])
  const isDarkMode = computed(() => $q.dark.isActive)
  return { MAP, isDarkMode }
}
