import streamlit as st

# Appliquer du CSS pour personnaliser l'affichage
def add_custom_css():
    st.markdown("""
        <style>
            .main { background-color: #f5f5f5; }
            .stButton>button { background-color: #ff6600; color: white; border-radius: 8px; }
            .stTitle { color: #333333; }
            .stMarkdown { font-size: 18px; }
        </style>
    """, unsafe_allow_html=True)

add_custom_css()

def calculate_roas_breakeven(cost_product, fixed_costs, variable_costs_percentage, selling_price_ht, units_sold):
    if selling_price_ht == 0:
        return "Le prix de vente ne peut pas être zéro."
    
    fixed_costs_per_unit = fixed_costs / units_sold if units_sold > 0 else 0
    total_variable_costs = (variable_costs_percentage / 100) * selling_price_ht
    roas_breakeven = (cost_product + fixed_costs_per_unit + total_variable_costs) / selling_price_ht
    return round(roas_breakeven, 2)

# Interface utilisateur avec Streamlit
st.title("Calculateur de ROAS Breakeven")

# Sélection du type d'activité
type_activite = st.selectbox("Choisissez votre type d'activité", ["E-commerce", "Lead Generation"])

# Inputs utilisateur
selling_price_ht = st.number_input("Prix de vente HT (€)", min_value=0.01, value=100.0, step=0.01)
cost_product = st.number_input("Coût du produit (€)", min_value=0.0, value=30.0, step=0.01)
fixed_costs = st.number_input("Charges fixes mensuelles (€)", min_value=0.0, value=5000.0, step=0.01)
variable_costs_percentage = st.number_input("Total des charges variables (% du CA)", min_value=0.0, max_value=100.0, value=18.0, step=0.1)
units_sold = st.number_input("Nombre d'unités vendues par mois", min_value=1, value=200, step=1)

# Affichage des recommandations selon le type d'activité
if type_activite == "Lead Generation":
    st.markdown("""<h3 style='color: #ff6600;'>Recommandations Lead Gen</h3>
    <ul>
    <li>Optimisez vos coûts d'acquisition par lead</li>
    <li>Suivez le taux de conversion des leads en clients</li>
    <li>Maximisez le retour sur investissement en affinant votre ciblage</li>
    </ul>
    """, unsafe_allow_html=True)

if type_activite == "E-commerce":
    st.markdown("""<h3 style='color: #ff6600;'>Recommandations E-commerce</h3>
    <ul>
    <li>Diminuez les frais variables (frais de transaction, logistique...)</li>
    <li>Optimisez votre taux de conversion sur le site</li>
    <li>Testez différentes stratégies d'enchères sur Google Ads</li>
    </ul>
    """, unsafe_allow_html=True)

# Calcul et affichage du ROAS Breakeven
if st.button("Calculer le ROAS Breakeven"):
    roas_breakeven = calculate_roas_breakeven(cost_product, fixed_costs, variable_costs_percentage, selling_price_ht, units_sold)
    st.success(f"ROAS Breakeven : {roas_breakeven} (soit {round(1/roas_breakeven, 2)}x du coût pub pour 1€ de CA)")
