<template>
    <div class="search-container">
      <div class="search-box">
        <input 
          v-model="searchQuery" 
          @input="debouncedSearch" 
          placeholder="Digite o nome da operadora..."
          class="search-input"
        />
        <button @click="performSearch" class="search-button">
          <span v-if="!loading">Buscar</span>
          <span v-else class="spinner"></span>
        </button>
      </div>
      
      <div v-if="error" class="error-message">
        {{ error }}
      </div>
      
      <div v-if="results.length > 0" class="results-section">
        <h2>Resultados encontrados: {{ results.length }}</h2>
        <div class="results-grid">
          <div v-for="(item, index) in results" :key="index" class="result-card">
            <h3>{{ item.Razao_Social }}</h3>
            <div class="card-body">
              <p><strong>CNPJ:</strong> {{ formatCNPJ(item.CNPJ) }}</p>
              <p><strong>Modalidade:</strong> {{ item.Modalidade }}</p>
              <p><strong>Cidade/UF:</strong> {{ item.Cidade }}/{{ item.UF }}</p>
              <p><strong>Similaridade:</strong> {{ item.similarity_score }}%</p>
              <div class="contact-info">
                <p v-if="item.Telefone"><strong>Telefone:</strong> ({{ item.DDD }}) {{ item.Telefone }}</p>
                <p v-if="item.Endereco_eletronico"><strong>Email:</strong> {{ item.Endereco_eletronico }}</p>
              </div>
            </div>
          </div>
        </div>
      </div>
      
      <div v-else-if="searchPerformed && !loading" class="no-results">
        Nenhum resultado encontrado para "{{ searchQuery }}"
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  import _ from 'lodash';
  
  export default {
    name: 'SearchOperadoras',
    data() {
      return {
        searchQuery: '',
        results: [],
        loading: false,
        error: null,
        searchPerformed: false
      };
    },
    created() {
      
      this.debouncedSearch = _.debounce(this.performSearch, 500);
    },
    methods: {
      formatCNPJ(cnpj) {
        if (!cnpj && cnpj !== 0) return 'Não informado';
        try {
          const cnpjStr = cnpj.toString().replace(/\D/g, '').padStart(14, '0');
          return cnpjStr.replace(/^(\d{2})(\d{3})(\d{3})(\d{4})(\d{2})$/, '$1.$2.$3/$4-$5');
        } catch (e) {
          console.error('Erro ao formatar CNPJ:', e);
          return 'Formato inválido';
        }
      },
      async performSearch() {
        this.loading = true;
        this.error = null;
        
        try {
          const response = await axios.get('http://localhost:5000/api/search', {
            params: {
              q: this.searchQuery,
              limit: 20
            },
            headers: {
              'Accept': 'application/json',
              'Content-Type': 'application/json'
            }
          });
          
          this.results = response.data;
          
        } catch (error) {
          console.error("Erro completo:", error);
          if (error.response) {
            this.error = `Erro ${error.response.status}: ${error.response.data?.error || 'Erro no servidor'}`;
          } else {
            this.error = "Não foi possível conectar ao servidor. Verifique se o backend está rodando.";
          }
        } finally {
          this.loading = false;
        }
      }

    }
  };
  </script>
  
  <style scoped>
  .search-container {
    max-width: 1000px;
    margin: 0 auto;
  }
  
  .search-box {
    display: flex;
    margin-bottom: 20px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
    border-radius: 4px;
    overflow: hidden;
  }
  
  .search-input {
    flex: 1;
    padding: 12px 15px;
    font-size: 16px;
    border: 1px solid #ddd;
    border-right: none;
    outline: none;
  }
  
  .search-input:focus {
    border-color: #42b983;
  }
  
  .search-button {
    padding: 0 20px;
    background-color: #42b983;
    color: white;
    border: none;
    cursor: pointer;
    font-size: 16px;
    font-weight: bold;
    transition: background-color 0.3s;
    display: flex;
    align-items: center;
    justify-content: center;
    min-width: 100px;
  }
  
  .search-button:hover {
    background-color: #369f6e;
  }
  
  .spinner {
    display: inline-block;
    width: 20px;
    height: 20px;
    border: 3px solid rgba(255, 255, 255, 0.3);
    border-radius: 50%;
    border-top-color: #fff;
    animation: spin 1s ease-in-out infinite;
  }
  
  @keyframes spin {
    to { transform: rotate(360deg); }
  }
  
  .error-message {
    color: #e74c3c;
    background-color: #fdecea;
    padding: 10px 15px;
    border-radius: 4px;
    margin-bottom: 20px;
  }
  
  .results-section {
    margin-top: 30px;
  }
  
  .results-section h2 {
    color: #2c3e50;
    margin-bottom: 15px;
    font-size: 1.2rem;
  }
  
  .results-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
    gap: 20px;
  }
  
  .result-card {
    background: white;
    border-radius: 8px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
    overflow: hidden;
    transition: transform 0.3s;
  }
  
  .result-card:hover {
    transform: translateY(-5px);
  }
  
  .result-card h3 {
    background-color: #42b983;
    color: white;
    margin: 0;
    padding: 15px;
    font-size: 1.1rem;
  }
  
  .card-body {
    padding: 15px;
  }
  
  .card-body p {
    margin: 8px 0;
    color: #555;
  }
  
  .contact-info {
    margin-top: 15px;
    padding-top: 15px;
    border-top: 1px solid #eee;
  }
  
  .no-results {
    text-align: center;
    padding: 30px;
    color: #666;
    font-size: 1.1rem;
  }
  </style>