# index.py
# Point d'entrée Streamlit résilient : routeur central qui charge des modules pages.
# Usage: streamlit run index.py

import streamlit as st
import importlib.util
from pathlib import Path
import traceback

st.set_page_config(
    page_title="TYNORA SIGN IN",
    page_icon="https://img.icons8.com/ios-filled/50/t-key.png",
    layout="wide",
    initial_sidebar_state="expanded",
)

BASE_DIR = Path(__file__).parent

def load_module_and_show(module_name: str):
    """Charge dynamiquement module_name.py et appelle sa fonction show()."""
    module_path = BASE_DIR / f"{module_name}.py"
    if not module_path.exists():
        st.error(f"Page introuvable: {module_name}.py")
        return
    try:
        spec = importlib.util.spec_from_file_location(module_name, str(module_path))
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        if hasattr(module, "show") and callable(module.show):
            module.show()
        else:
            st.error(f"Le module {module_name}.py doit définir une fonction show()")
    except Exception as e:
        st.error("Erreur lors du chargement de la page.")
        st.exception(e)

# Récupérer le paramètre page depuis l'URL de façon sûre
def get_page_param(default="signin"):
    try:
        query = st.experimental_get_query_params()
        page = query.get("page", [default])[0]
        return page
    except Exception:
        # Fallback : si experimental_get_query_params n'est pas disponible ou lève une erreur,
        # on utilise st.session_state pour conserver la page courante.
        if "page" not in st.session_state:
            st.session_state.page = default
        return st.session_state.page

# Permettre de changer la page via boutons sidebar (optionnel)
st.sidebar.title("Navigation")
if st.sidebar.button("Sign in"):
    st.experimental_set_query_params(page="signin")
if st.sidebar.button("Sign up"):
    st.experimental_set_query_params(page="signup")
if st.sidebar.button("Forgot"):
    st.experimental_set_query_params(page="forgot")
if st.sidebar.button("Feed"):
    st.experimental_set_query_params(page="feed")

# Obtenir la page demandée (avec fallback)
page = get_page_param()

# Si la page demandée est signin, on affiche l'HTML intégré (ton ancien index.html converti)
if page == "signin":
    import streamlit.components.v1 as components
    html = """<!DOCTYPE html>
    <html lang="fr">
    <head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Tynorah — Sign In</title>
    <style>
      html,body{height:100%;margin:0;font-family:Inter,system-ui,Arial;}
      body{background:#f5f5f5;position:relative;min-height:100vh;}
      .container{width:450px;max-width:92vw;background:#fff;border-radius:60px;box-shadow:0 6px 18px rgba(0,0,0,0.1);position:absolute;padding:20px;box-sizing:border-box;}
      .header{text-align:center;margin-bottom:12px;}
      .brand{font-weight:800;letter-spacing:4px;color:#111827;margin-bottom:6px;}
      h1{margin:0;font-size:28px;font-weight:800;}
      .subtitle{color:#6b7280;margin-top:6px;font-size:14px;}
      label{display:block;margin-top:12px;font-weight:700;font-size:13px;color:#111827;}
      input[type="email"], input[type="password"], input[type="text"]{width:100%;padding:12px;border-radius:8px;border:1.5px solid #e6e6eb;background:#fafafa;margin-top:6px;box-sizing:border-box;}
      .terms{display:flex;align-items:center;gap:10px;margin-top:12px;}
      .btn{margin-top:30px;padding:12px;border-radius:10px;border:none;background:linear-gradient(90deg,#7800F6,#1465FF);color:#fff;font-weight:800;cursor:pointer;width:100%;}
      .small{text-align:center;margin-top:14px;color:#6b7280;font-size:13px;}
      .signin-link{color:#6b46ff;text-decoration:none;font-weight:700;}
      a.signin-link-small{font-size:11px;color:#6b46ff;text-decoration:none;}
    </style>
    </head>
    <body>
    <div class="container" id="auth-container">
      <header class="header"><div class="brand">TYNORAH</div><h1>LOGIN</h1><p class="subtitle">Enter your details to access your account</p></header>
      <form id="login-form" onsubmit="return handleSubmit(event);">
        <label for="login-email">Email</label>
        <input id="login-email" name="email" type="email" autocomplete="username" placeholder="example@email.com" required>
        <div style="display:flex;justify-content:space-between;align-items:flex-end;">
          <label for="login-password">Password</label>
          <a href="?page=forgot" class="signin-link-small">Forgot password?</a>
        </div>
        <input id="login-password" name="password" type="password" autocomplete="current-password" placeholder="•••••••••••••" required>
        <div class="terms"><input id="remember" type="checkbox"><label for="remember">Remember me</label></div>
        <button class="btn" type="submit">SIGN IN</button>
        <p class="small">Don't have an account? <a href="?page=signup" class="signin-link">Sign up</a></p>
      </form>
    </div>
    <script>
      function centerContainer(){
        const c = document.getElementById('auth-container');
        if(!c) return;
        const left = Math.max((window.innerWidth - c.offsetWidth)/2, 12);
        const top = Math.max((window.innerHeight - c.offsetHeight)/2, 12);
        c.style.left = left + 'px'; c.style.top = top + 'px';
      }
      window.addEventListener('load', centerContainer);
      window.addEventListener('resize', centerContainer);

      function handleSubmit(e){
        e.preventDefault();
        const email = document.getElementById('login-email').value.trim();
        const password = document.getElementById('login-password').value.trim();
        if(!email || !password){ alert("Veuillez entrer vos identifiants."); return false; }
        // navigation via query param -> index.py routeur prendra page=feed
        window.location.search = '?page=feed';
        return false;
      }
    </script>
    </body></html>
    """
    import streamlit.components.v1 as components
    components.html(html, height=900, scrolling=True)

# Si page != signin, on tente de charger un module du même nom (signup, forgot, feed, etc.)
else:
    allowed = {"signup", "forgot", "feed"}
    if page not in allowed:
        st.error("Page non autorisée.")
    else:
        # Mettre à jour st.session_state.page pour fallback si experimental_get_query_params échoue plus tard
        st.session_state.page = page
        load_module_and_show(page)
