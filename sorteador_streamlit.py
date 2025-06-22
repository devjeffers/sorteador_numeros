import streamlit as st
import random

# Título da página
st.title("🎲 Sorteador de Números Únicos")

# Inicializa os dados na sessão do usuário
if 'numeros_disponiveis' not in st.session_state:
    st.session_state.numeros_disponiveis = list(range(1, 150))
    st.session_state.sorteados = []

# Botão para sortear número
if st.button("🎯 Sortear Número"):
    if st.session_state.numeros_disponiveis:
        numero = random.choice(st.session_state.numeros_disponiveis)
        st.session_state.numeros_disponiveis.remove(numero)
        st.session_state.sorteados.append(numero)
        st.success(f"Número sorteado: **{numero}**")
    else:
        st.warning("Todos os números já foram sorteados! Clique em '🔁 Resetar Sorteio' para começar novamente.")

# Mostrar os números já sorteados
if st.session_state.sorteados:
    st.subheader("📋 Números Sorteados:")
    st.write(st.session_state.sorteados)

# Botão para resetar o sorteio
if st.button("🔁 Resetar Sorteio"):
    st.session_state.numeros_disponiveis = list(range(1, 150))
    st.session_state.sorteados = []
    st.info("Sorteio reiniciado com sucesso!")
