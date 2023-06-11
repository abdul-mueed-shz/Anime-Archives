import { computed } from 'vue'
import { useStore } from 'vuex'

export default function useComputes () {
  const store = useStore()
  const MAP = computed(() => store.getters['translations/getMap'])
  return { MAP }
}
