# 🐛 Debug com IA: Identificação e Correção de Erros

## 📋 Índice
1. [Código Original com Erros](#código-original-com-erros)
2. [Identificação dos Erros](#identificação-dos-erros)
3. [Explicação Detalhada de Cada Erro](#explicação-detalhada-de-cada-erro)
4. [Código Corrigido](#código-corrigido)
5. [Comparação: Antes vs. Depois](#comparação-antes-vs-depois)
6. [Checklist de Debugging](#checklist-de-debugging)

---

## Código Original com Erros

```python
# ENTRADA DE DADOS
cliente = input("Qual é seu nome? ")

qtd1 = int(input("Quantidade do item 1: "))
item1 = float(input(Preço do item 1? ))  # ❌ ERRO 1: Aspas faltando

qtd2 = int(input("Quantidade do item 2: "))
item2 = float(input("Preço do item 2? "))

qtd3 = int(input("Quantidade do item 3: "))
item3 = float(input("Preço do item 3? "))

# CÁLCULOS DOS ITENS
total_item1 = qtd1 * item1
total_item2 = qtd2 * item2
total_item3 = qtd3 * item3

subtotal = total_item1 + total_item2 + total_item3
imposto = subtotal * 0.10

# DESCONTO
desconto_cupom = (input("Você tem um cupom de desconto? (Digite o percentual ou 0): "))
desconto = subtotal * (desconto_cupom / 100)  # ❌ ERRO 2: String em operação matemática

# TOTAL FINAL
total = subtotal + imposto - desconto

# EXIBIÇÃO
linha = "=" * 31
separador = "-" * 31

print(linha)
print(f" Cliente: {cliente}")
print(linha)
print(f" Item 1:        R$ {total_item1:.2f}")
print(" Item 2:        R$ {total_item2:.2f}")  # ❌ ERRO 3: f-string faltando
print(f" Item 3:        R$ {total_item3:.2f}")
print(separador)
print(f" Subtotal:      R$ {subtotal:.2f}")
print(f" Imposto (10%): R$ {imposto:.2f}")

if desconto_cupom > 0:  # ❌ ERRO 4: Comparação string com número
    print(f" Desconto ({desconto_cupom:.0f}%): -R$ {desconto:.2f}")  # ❌ ERRO 5: Indentação incorreta

print(linha)
print(f" TOTAL:         R$ {round(total, 2):.2f}")
print(linha)
```

---

## Identificação dos Erros

### 🔴 Resumo Rápido

| # | Tipo | Linha | Erro | Severidade |
|---|------|-------|------|-----------|
| 1 | **Sintaxe** | 5 | Aspas faltando em string | 🔴 CRÍTICO |
| 2 | **Tipo** | 21 | String em operação matemática | 🔴 CRÍTICO |
| 3 | **Sintaxe** | 31 | f-string faltando | 🟠 ALTO |
| 4 | **Tipo** | 35 | Comparar string com número | 🔴 CRÍTICO |
| 5 | **Indentação** | 36 | Bloco if sem indentação | 🔴 CRÍTICO |

---

## Explicação Detalhada de Cada Erro

### ❌ ERRO 1: Aspas Faltando (Linha 5)

```python
# ❌ ERRADO
item1 = float(input(Preço do item 1? ))

# ❌ Mensagem de erro:
# SyntaxError: invalid syntax
# "Preço do item 1?" é visto como múltiplas variáveis, não como string
```

**Por quê?**
- `input()` recebe uma string como parâmetro
- Sem aspas, Python tenta interpretar `Preço`, `do`, `item`, `1` como variáveis
- Variáveis não existem → SyntaxError

**Correção:**
```python
# ✅ CORRETO
item1 = float(input("Preço do item 1? "))  # Adicione aspas duplas
# ou
item1 = float(input('Preço do item 1? '))  # Aspas simples também funcionam
```

---

### ❌ ERRO 2: String em Operação Matemática (Linha 21)

```python
# ❌ PROBLEMA
desconto_cupom = (input("Você tem um cupom de desconto? (Digite o percentual ou 0): "))
# input() retorna STRING, não número
# "50" ≠ 50

desconto = subtotal * (desconto_cupom / 100)
# ❌ Mensagem de erro:
# TypeError: unsupported operand type(s) for /: 'str' and 'int'
# Não pode dividir string por número!
```

**Por quê?**
- `input()` **sempre** retorna string
- `"50"` é diferente de `50`
- String + operação matemática = TypeError

**Correção:**
```python
# ✅ CORRETO - Converter para float
desconto_cupom = float(input("Você tem um cupom de desconto? (Digite o percentual ou 0): "))
# Agora "50" vira 50.0 e pode fazer operações matemáticas
```

**Exemplo:**
```python
# ❌ Errado
texto = "50"
resultado = texto / 100  # TypeError!

# ✅ Certo
numero = float("50")  # Converte string em número
resultado = numero / 100  # 0.5 ✅
```

---

### ❌ ERRO 3: f-string Faltando (Linha 31)

```python
# ❌ ERRADO - Sem 'f' antes da string
print(" Item 2:        R$ {total_item2:.2f}")
# Saída: Item 2:        R$ {total_item2:.2f}
# ❌ Imprime literalmente, não substitui a variável

# ✅ CORRETO - Com 'f' antes da string
print(f" Item 2:        R$ {total_item2:.2f}")
# Saída: Item 2:        R$ 50.00
# ✅ Substitui {total_item2:.2f} pelo valor formatado
```

**Por quê?**
- f-string (formatted string literal) é indicada pelo prefixo `f`
- Sem o `f`, Python trata como string normal
- Expressões em `{}` não são avaliadas

**Exemplo:**
```python
preco = 50.5

# ❌ String comum
print("Preço: {preco}")  # Preço: {preco}

# ✅ f-string
print(f"Preço: {preco}")  # Preço: 50.5

# ✅ f-string com formatação
print(f"Preço: {preco:.2f}")  # Preço: 50.50
```

---

### ❌ ERRO 4: Comparar String com Número (Linha 35)

```python
# ❌ PROBLEMA
desconto_cupom = (input("..."))  # Retorna STRING "50"
if desconto_cupom > 0:  # ❌ Comparando string com número
    print(...)
# TypeError: '>' not supported between instances of 'str' and 'int'
```

**Por quê?**
- `desconto_cupom` é string (ex: `"50"`)
- Python não consegue comparar string com número
- Precisa converter antes

**Correção:**
```python
# ✅ Já convertemos na Linha 21 (ERRO 2)
desconto_cupom = float(input("..."))  # Agora é número (50.0)
if desconto_cupom > 0:  # ✅ Comparação válida
    print(...)
```

**Exemplo:**
```python
# ❌ Errado
texto = "50"
if texto > 0:  # TypeError!
    pass

# ✅ Certo
numero = float("50")
if numero > 0:  # ✅ Funciona
    pass
```

---

### ❌ ERRO 5: Indentação Incorreta (Linha 36)

```python
# ❌ ERRADO - Sem indentação
if desconto_cupom > 0:
print(f" Desconto ({desconto_cupom:.0f}%): -R$ {desconto:.2f}")
# IndentationError: expected an indented block

# ✅ CORRETO - Com indentação
if desconto_cupom > 0:
    print(f" Desconto ({desconto_cupom:.0f}%): -R$ {desconto:.2f}")
```

**Por quê?**
- Python usa indentação para definir blocos de código
- `if`, `for`, `while`, `def`, etc. exigem indentação
- Sem indentação → IndentationError

**Convenção:**
```python
# ✅ 4 espaços (recomendado pela PEP 8)
if condicao:
    comando_1
    comando_2

# ⚠️ Tab também funciona, mas não misture com espaços
if condicao:
	comando_1  # ⚠️ Tab (evite)

# ❌ Sem indentação
if condicao:
comando_1  # ❌ Erro!
```

---

## Código Corrigido

```python
# ENTRADA DE DADOS
cliente = input("Qual é seu nome? ")

qtd1 = int(input("Quantidade do item 1: "))
item1 = float(input("Preço do item 1? "))  # ✅ CORRIGIDO: Aspas adicionadas

qtd2 = int(input("Quantidade do item 2: "))
item2 = float(input("Preço do item 2? "))

qtd3 = int(input("Quantidade do item 3: "))
item3 = float(input("Preço do item 3? "))

# CÁLCULOS DOS ITENS
total_item1 = qtd1 * item1
total_item2 = qtd2 * item2
total_item3 = qtd3 * item3

subtotal = total_item1 + total_item2 + total_item3
imposto = subtotal * 0.10

# DESCONTO
desconto_cupom = float(input("Você tem um cupom de desconto? (Digite o percentual ou 0): "))  # ✅ CORRIGIDO: Convertido para float
desconto = subtotal * (desconto_cupom / 100)

# TOTAL FINAL
total = subtotal + imposto - desconto

# EXIBIÇÃO
linha = "=" * 31
separador = "-" * 31

print(linha)
print(f" Cliente: {cliente}")
print(linha)
print(f" Item 1:        R$ {total_item1:.2f}")
print(f" Item 2:        R$ {total_item2:.2f}")  # ✅ CORRIGIDO: f-string adicionada
print(f" Item 3:        R$ {total_item3:.2f}")
print(separador)
print(f" Subtotal:      R$ {subtotal:.2f}")
print(f" Imposto (10%): R$ {imposto:.2f}")

if desconto_cupom > 0:  # ✅ CORRIGIDO: Agora desconto_cupom é float
    print(f" Desconto ({desconto_cupom:.0f}%): -R$ {desconto:.2f}")  # ✅ CORRIGIDO: Indentação adicionada

print(linha)
print(f" TOTAL:         R$ {round(total, 2):.2f}")
print(linha)
```

---

## Comparação: Antes vs. Depois

### Resumo Visual

```
ANTES (❌ Com Erros)          DEPOIS (✅ Corrigido)
─────────────────────────     ──────────────────────
Linha 5:  input(Preço...)     input("Preço...")
Linha 21: input(...) string   float(input(...))
Linha 31: print(" Item 2:...  print(f" Item 2:...
Linha 35: if string > 0       if float > 0
Linha 36: print(...) 0 indent print(...) 4 indent
```

---

## Tabela de Erros e Correções

| # | Tipo | Linha | Erro | Correção | Por quê |
|---|------|-------|------|----------|---------|
| 1 | SyntaxError | 5 | `input(Preço...)` | `input("Preço...")` | String precisa de aspas |
| 2 | TypeError | 21 | `input()` retorna string | `float(input())` | input() precisa conversão |
| 3 | Lógica | 31 | Sem `f` em string | `f" Item 2:..."` | f-string precisa do `f` |
| 4 | TypeError | 35 | String > número | Já corrigido em #2 | Tipo de dado incompatível |
| 5 | IndentationError | 36 | Sem indentação | 4 espaços no print | Python exige indentação |

---

## Checklist de Debugging

### ✅ Tipos de Erro Encontrados

- [x] **SyntaxError** - Aspas faltando (Erro #1)
- [x] **TypeError** - Operação com tipo incompatível (Erro #2)
- [x] **Lógica** - f-string faltando (Erro #3)
- [x] **TypeError** - Comparação tipo incompatível (Erro #4)
- [x] **IndentationError** - Indentação incorreta (Erro #5)

### ✅ Processo de Debug

- [x] Identificar tipo de erro
- [x] Localizar linha exata
- [x] Explicar causa raiz
- [x] Fornecer correção
- [x] Explicar por que funciona
- [x] Fornecer exemplo similar

### ✅ Boas Práticas Aplicadas

- [x] Conversão de tipos explícita (`float()`, `int()`)
- [x] Strings com aspas duplas (convenção)
- [x] f-strings para formatação moderna
- [x] Indentação correta (4 espaços)
- [x] Comentários indicando erros

---

## Lições Aprendidas

### 🎯 Conceitos-Chave

1. **input() sempre retorna string**
   - Use `int()`, `float()` para converter
   - Nunca confie no tipo de entrada

2. **f-strings vs strings comuns**
   - f-string: `f"Valor: {variavel}"`
   - String comum: `"Valor: {variavel}"` (literal)

3. **Indentação em Python**
   - Obrigatória após `:` (if, for, while, etc.)
   - Use 4 espaços (convenção PEP 8)
   - Não misture tabs com espaços

4. **Type checking**
   - Cuidado ao comparar tipos diferentes
   - `"50" ≠ 50`
   - Converta antes de usar

5. **Leitura de mensagens de erro**
   - SyntaxError: problema na estrutura
   - TypeError: tipo incompatível
   - IndentationError: indentação incorreta

---

## Exemplo Completo de Execução

### Entrada do Usuário:
```
Qual é seu nome? João Silva
Quantidade do item 1: 2
Preço do item 1? 25.50
Quantidade do item 2: 1
Preço do item 2? 100.00
Quantidade do item 3: 3
Preço do item 3? 15.75
Você tem um cupom de desconto? (Digite o percentual ou 0): 10
```

### Saída Esperada:
```
===============================
 Cliente: João Silva
===============================
 Item 1:        R$ 51.00
 Item 2:        R$ 100.00
 Item 3:        R$ 47.25
-------------------------------
 Subtotal:      R$ 198.25
 Imposto (10%): R$ 19.82
 Desconto (10%): -R$ 19.82
===============================
 TOTAL:         R$ 198.25
===============================
```

---

## Dicas para Evitar Erros

✅ **Sempre converter input():**
```python
idade = int(input("Sua idade? "))  # ✅ Converte
desconto = float(input("Desconto? "))  # ✅ Converte
```

✅ **Use f-strings para formatação:**
```python
print(f"Valor: R$ {preco:.2f}")  # ✅ f-string
# Não use:
print("Valor: R$ {preco:.2f}")  # ❌ Sem f
```

✅ **Indente blocos de código:**
```python
if condicao:
    print("Dentro do if")  # ✅ 4 espaços
print("Fora do if")  # ✅ Sem indentação
```

✅ **Use aspas em strings:**
```python
texto = "Isto é uma string"  # ✅
numero = 42  # ✅ Número não precisa aspas
```

---

**Conclusão:** Todos os 5 erros foram identificados, explicados e corrigidos! 🎉

**Data:** 2026-04-29  
**Versão:** 1.0 (Debug Completo)
