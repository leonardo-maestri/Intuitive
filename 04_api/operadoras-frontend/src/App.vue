<template>
  <div class="app-container">
    <header>
      <h1>Busca de Operadoras de Saúde</h1>
    </header>
    <main>
      <SearchOperadoras />
    </main>
  </div>
</template>

<script>
import SearchOperadoras from './components/SearchOperadoras.vue'

export default {
  name: 'App',
  components: {
    SearchOperadoras
  }
}
</script>

<style>
.app-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
  font-family: Arial, sans-serif;
}

header {
  text-align: center;
  margin-bottom: 30px;
}

header h1 {
  color: #2c3e50;
}
</style>