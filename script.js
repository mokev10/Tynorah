/* ============================================================
   TYNORAH - SCRIPT GLOBAL FINAL (script.js)
   ============================================================ */
document.addEventListener('DOMContentLoaded', () => {

  /* ================= 1. TABS PROFIL ================= */
  const tabs = document.querySelectorAll(".tab");
  const contents = document.querySelectorAll(".tab-content");

  function hideAllSections() {
    contents.forEach(c => c.classList.remove("active"));
    tabs.forEach(t => t.classList.remove("active"));
  }

  tabs.forEach(tab => {
    tab.addEventListener("click", function(e){
      e.preventDefault(); // empêche le scroll vers l'ancre
      hideAllSections();
      this.classList.add("active");
      const target = document.querySelector(this.getAttribute("href"));
      if(target) target.classList.add("active");
    });
  });

  // ✅ Initialisation : garder PUBLICATIONS par défaut
  // On vérifie si aucun tab n'est actif, alors on active le premier
  const activeTab = document.querySelector(".tab.active");
  if (!activeTab && tabs.length > 0) {
    tabs[0].classList.add("active");
    const firstTarget = document.querySelector(tabs[0].getAttribute("href"));
    if (firstTarget) firstTarget.classList.add("active");
  }

});


document.addEventListener('DOMContentLoaded', () => {
    
    /* ============================================================
       1. GESTION DE LA RECHERCHE (GLASS UI)
       ============================================================ */
    const searchBtn = document.getElementById('search-nav-btn'); // Ton bouton loupe
    const searchWrapper = document.querySelector('.search-wrapper');
    const searchClose = document.querySelector('.search-close');
    const searchInput = document.getElementById('searchInput');

    if (searchBtn && searchWrapper) {
        // Ouvrir la recherche
        searchBtn.addEventListener('click', (e) => {
            e.preventDefault();
            searchWrapper.classList.add('active');
            searchInput.focus(); // Met le curseur direct dans la barre
            document.body.style.overflow = 'hidden'; // Empêche de scroller le feed derrière
        });

        // Fermer la recherche
        const closeSearch = () => {
            searchWrapper.classList.remove('active');
            document.body.style.overflow = 'auto'; // Réactive le scroll
        };

        searchClose.addEventListener('click', closeSearch);

        // Fermer si on clique sur le fond flou (en dehors de la barre)
        searchWrapper.addEventListener('click', (e) => {
            if (e.target === searchWrapper) closeSearch();
        });

        // Fermer avec la touche Echap
        document.addEventListener('keydown', (e) => {
            if (e.key === "Escape") closeSearch();
        });
    }

    /* ============================================================
       2. GESTION DU FEED (LIKE & ACTIONS)
       ============================================================ */
    const feedContainer = document.querySelector('.feed-container');

    if (feedContainer) {
        feedContainer.addEventListener('click', (e) => {
            const target = e.target;

            // Système de Like (animation simple)
            if (target.closest('.action-btn')) {
                const btn = target.closest('.action-btn');
                // Si c'est le bouton like (on imagine que l'image change ou scale)
                btn.style.transform = 'scale(1.3)';
                setTimeout(() => {
                    btn.style.transform = 'scale(1)';
                }, 150);
                
                // Ici tu pourras ajouter la logique pour changer l'icône coeur
                // exemple: btn.querySelector('img').src = 'icons/heart-filled.png';
            }
        });
    }

    /* ============================================================
       3. NAVIGATION ACTIVE (HIGHLIGHT)
       ============================================================ */
    const navItems = document.querySelectorAll('.nav-item');
    
    navItems.forEach(item => {
        item.addEventListener('click', function() {
            navItems.forEach(i => i.classList.remove('active'));
            this.classList.add('active');
        });
    });

    /* ============================================================
       4. SIMULATION DE RECHERCHE (SUGGESTIONS)
       ============================================================ */
    if (searchInput) {
        const dropdown = document.querySelector('.suggestions-dropdown');

        searchInput.addEventListener('input', (e) => {
            if (e.target.value.length > 0) {
                dropdown.style.display = 'block';
            } else {
                dropdown.style.display = 'none';
            }
        });
    }
});


/* ============================================================
   REDIRECTION VERS LE PROFIL
   ============================================================ */
const goToProfile = () => {
    // Redirige vers la page profile.html
    window.location.href = 'profile.html';
};

// On cible le bouton profil dans la navigation
const profileBtn = document.querySelector('.nav-item-profile'); 
// Note : j'ajoute une classe spécifique pour être sûr

if (profileBtn) {
    profileBtn.addEventListener('click', (e) => {
        e.preventDefault(); // Empêche le comportement par défaut si c'est un lien <a>
        goToProfile();
    });
}

// Optionnel : Si tu as aussi une mini-avatar dans la "user-zone" en haut à droite
const miniAvatar = document.querySelector('.mini-avatar');
if (miniAvatar) {
    miniAvatar.style.cursor = 'pointer';
    miniAvatar.addEventListener('click', goToProfile);
}


/* ============================================================
   GESTION DES RÉACTIONS (LIKE)
   ============================================================ */
function toggleLike(btn) {
    const img = btn.querySelector('img');
    const isLiked = btn.classList.toggle('liked'); // On switch une classe 'liked'
    
    const activeSrc = img.getAttribute('data-active');
    const inactiveSrc = img.getAttribute('data-inactive');

    if (isLiked) {
        img.src = activeSrc;
        btn.style.transform = 'scale(1.3)'; // Petit effet de bond
        btn.style.filter = 'drop-shadow(0 0 5px rgba(255,0,0,0.3))';
    } else {
        img.src = inactiveSrc;
        btn.style.transform = 'scale(1)';
        btn.style.filter = 'none';
    }
    
    // Reset de l'échelle après l'animation
    setTimeout(() => {
        if(isLiked) btn.style.transform = 'scale(1.1)';
        else btn.style.transform = 'scale(1)';
    }, 150);
}

/* ============================================================
   GESTION DES COMMENTAIRES
   ============================================================ */
document.addEventListener('DOMContentLoaded', () => {
    // 1. Afficher/Masquer la section commentaire
    const commentBtns = document.querySelectorAll('.comment-toggle-btn');
    
    commentBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            const postCard = btn.closest('.post-card');
            const commentSection = postCard.querySelector('.comments-section');
            
            // Toggle l'affichage
            if (commentSection.style.display === 'none' || commentSection.style.display === '') {
                commentSection.style.display = 'block';
                commentSection.querySelector('.comment-input').focus();
            } else {
                commentSection.style.display = 'none';
            }
        });
    });

    // 2. Publier un commentaire
    const publishBtns = document.querySelectorAll('.publish-comment-btn');

    publishBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            const postCard = btn.closest('.post-card');
            const input = postCard.querySelector('.comment-input');
            const list = postCard.querySelector('.comments-list');

            if (input.value.trim() !== "") {
                const newComment = document.createElement('div');
                newComment.style.marginBottom = '8px';
                newComment.style.fontSize = '14px';
                
                // Structure du commentaire (nom en gras + texte)
                newComment.innerHTML = `<strong>Moi</strong> ${input.value}`;
                
                list.appendChild(newComment);
                input.value = ""; // Vide le champ
            }
        });
    });
});



document.addEventListener('DOMContentLoaded', () => {
    const editBtn = document.querySelector('.btn-profile'); // Le bouton Modifier
    const username = document.querySelector('.profile-username');
    const bio = document.querySelector('.profile-bio p');

    // 1. Charger les données sauvegardées au chargement de la page
    const savedUsername = localStorage.getItem('tynorah_username');
    const savedBio = localStorage.getItem('tynorah_bio');

    if (savedUsername) username.innerText = savedUsername;
    if (savedBio) bio.innerHTML = savedBio;

    // 2. Logique du bouton Modifier / Enregistrer
    editBtn.addEventListener('click', () => {
        const isEditing = username.contentEditable === "true";

        if (!isEditing) {
            // Passer en mode EDITION
            username.contentEditable = "true";
            bio.contentEditable = "true";
            
            username.classList.add('editing-mode');
            bio.classList.add('editing-mode');
            
            username.focus(); // Met le curseur directement sur le nom
            editBtn.innerText = "Enregistrer";
            editBtn.style.backgroundColor = "#3897f0"; // Couleur bleue pour "Enregistrer"
            editBtn.style.color = "#fff";
        } else {
            // Passer en mode SAUVEGARDE
            username.contentEditable = "false";
            bio.contentEditable = "false";
            
            username.classList.remove('editing-mode');
            bio.classList.remove('editing-mode');
            
            // Sauvegarder dans le navigateur
            localStorage.setItem('tynorah_username', username.innerText);
            localStorage.setItem('tynorah_bio', bio.innerHTML);
            
            editBtn.innerText = "Modifier le profil";
            editBtn.style.backgroundColor = "#efefef";
            editBtn.style.color = "#000";
            
            alert("Profil mis à jour !");
        }
    });
});



document.addEventListener('DOMContentLoaded', () => {

    /* ============================================================
       1. PAGE PROFIL : AFFICHAGE DES DONNÉES
       ============================================================ */
    const displayUsername = document.getElementById('display-username');
    const displayBio = document.getElementById('display-bio');

    // On vérifie si on est sur la page profil
    if (displayUsername && displayBio) {
        const savedName = localStorage.getItem('tynorah_username');
        const savedBio = localStorage.getItem('tynorah_bio');

        // Si des données existent dans la mémoire du navigateur, on les affiche
        if (savedName) {
            displayUsername.innerText = savedName;
        }
        if (savedBio) {
            displayBio.innerText = savedBio;
        }
    }

    /* ============================================================
       2. PAGE MODIFICATION : LOGIQUE DE SAUVEGARDE
       ============================================================ */
    const inputName = document.getElementById('edit-username');
    const inputBio = document.getElementById('edit-bio');
    const saveBtn = document.getElementById('save-profile');

    // On vérifie si on est sur la page modification
    if (inputName && inputBio && saveBtn) {
        
        // A. Remplir les champs avec les données actuelles (pour ne pas repartir de zéro)
        inputName.value = localStorage.getItem('tynorah_username') || "User_name";
        inputBio.value = localStorage.getItem('tynorah_bio') || "";

        // B. Action au clic sur le bouton Enregistrer
        saveBtn.addEventListener('click', () => {
            const newName = inputName.value.trim();
            const newBio = inputBio.value.trim();

            // Sécurité : on vérifie que le nom n'est pas vide
            if (newName === "") {
                alert("Le nom d'utilisateur ne peut pas être vide !");
                return;
            }

            // Sauvegarde dans le localStorage
            localStorage.setItem('tynorah_username', newName);
            localStorage.setItem('tynorah_bio', newBio);

            // Redirection immédiate vers le profil
            window.location.href = 'profile.html';
        });
    }

    /* ============================================================
       3. GESTION DES ONGLETS (PUBLICATIONS, REELS, ETC.)
       ============================================================ */
    const tabs = document.querySelectorAll('.tab');
    const contents = document.querySelectorAll('.tab-content');

    if (tabs.length > 0) {
        tabs.forEach(tab => {
            tab.addEventListener('click', (e) => {
                e.preventDefault();
                
                // Retirer la classe active de tous les onglets
                tabs.forEach(t => t.classList.remove('active'));
                // Masquer tous les contenus
                contents.forEach(c => c.style.display = 'none');

                // Activer l'onglet cliqué
                tab.classList.add('active');
                
                // Afficher le contenu correspondant (via l'ID dans le href)
                const targetId = tab.getAttribute('href').substring(1);
                const targetContent = document.getElementById(targetId);
                if (targetContent) {
                    targetContent.style.display = 'block';
                }
            });
        });
    }
});


document.addEventListener('DOMContentLoaded', () => {
    // Éléments de l'interface
    const modal = document.getElementById('edit-modal');
    const openBtn = document.getElementById('open-edit'); // Assure-toi que ton bouton a cet ID
    const closeBtn = document.getElementById('close-modal');
    const saveBtn = document.getElementById('save-profile');

    // Champs de texte
    const inputName = document.getElementById('edit-username');
    const inputBio = document.getElementById('edit-bio');
    const displayName = document.getElementById('display-username');
    const displayBio = document.getElementById('display-bio');

    // --- 1. CHARGEMENT INITIAL ---
    // On récupère les infos stockées au chargement de la page
    const savedName = localStorage.getItem('tynorah_username');
    const savedBio = localStorage.getItem('tynorah_bio');

    if (savedName) displayName.innerText = savedName;
    if (savedBio) displayBio.innerText = savedBio;

    // --- 2. OUVERTURE ---
    openBtn.addEventListener('click', (e) => {
        e.preventDefault();
        // On remplit les champs du formulaire avec les textes actuels du profil
        inputName.value = displayName.innerText;
        inputBio.value = displayBio.innerText;
        
        modal.style.display = 'flex'; // Affiche la modale
    });

    // --- 3. FERMETURE ---
    // Via le bouton "X"
    closeBtn.addEventListener('click', () => {
        modal.style.display = 'none';
    });

    // Via un clic n'importe où sur l'arrière-plan flou
    window.addEventListener('click', (e) => {
        if (e.target === modal) {
            modal.style.display = 'none';
        }
    });

    // --- 4. SAUVEGARDE ---
    saveBtn.addEventListener('click', () => {
        const newName = inputName.value.trim();
        const newBio = inputBio.value.trim();

        if (newName !== "") {
            // Sauvegarde locale
            localStorage.setItem('tynorah_username', newName);
            localStorage.setItem('tynorah_bio', newBio);
            
            // Mise à jour visuelle instantanée
            displayName.innerText = newName;
            displayBio.innerText = newBio;
            
            // On ferme la fenêtre
            modal.style.display = 'none';
        } else {
            alert("Le nom ne peut pas être vide.");
        }
    });
});



// Action bouton pour partager le profil

document.addEventListener('DOMContentLoaded', () => {
    const shareBtn = document.getElementById('share-profile-btn');

    if (shareBtn) {
        shareBtn.addEventListener('click', async () => {
            const shareData = {
                title: 'Tynorah',
                text: 'Découvre mon profil sur Tynorah !',
                url: window.location.href // Partage l'URL actuelle de la page
            };

            try {
                // Vérifie si le navigateur supporte le partage natif (Mobile)
                if (navigator.share) {
                    await navigator.share(shareData);
                    console.log('Profil partagé avec succès');
                } else {
                    // Alternative pour PC : Copier le lien dans le presse-papier
                    await navigator.clipboard.writeText(window.location.href);
                    alert('Lien du profil copié dans le presse-papier !');
                }
            } catch (err) {
                console.log('Erreur lors du partage :', err);
            }
        });
    }
});


document.addEventListener('DOMContentLoaded', () => {
    const statsModal = document.getElementById('stats-modal');
    const statsTitle = document.getElementById('stats-title');
    const statsList = document.getElementById('stats-list');
    const closeStats = document.getElementById('close-stats');

    // Données d'exemple (Simulées)
    const followers = [
        { name: 'Cristiano Ronaldo', username: 'cristiano', img: 'https://www.hebergeur-image.fr/uploads/20260317/50fe603e2912c910695f5f52770f351ddc24425a.jpg' },
        { name: 'Jude Bellingham', username: 'judebellingham', img: 'https://www.hebergeur-image.fr/uploads/20260317/6c4d469ebda121ba7a35c6db3000eb981db8be25.jpg' },
        { name: 'Marvel Studios', username: 'marvel', img: 'https://www.hebergeur-image.fr/uploads/20260317/d5033244822ebb78f5eb58ce46f316a0a5feb3d6.jpg' }
    ];

    const following = [
        { name: 'Lionel Messi', username: 'leomessi', img: 'https://www.hebergeur-image.fr/uploads/20260317/b69e2e13e905a6eb3d16420a1f56a11fd7a4255d.jpg' },
        { name: 'Netflix FR', username: 'netflixfr', img: 'https://www.hebergeur-image.fr/uploads/20260317/f19c1849f0d485a3853e6a51224a4512d5c4b7c4.jpg' }
    ];

    // Fonction pour afficher la liste
    function showStats(type) {
        statsTitle.innerText = type === 'followers' ? 'Abonnés' : 'Abonnements';
        const data = type === 'followers' ? followers : following;
        
        statsList.innerHTML = ''; // On vide la liste
        
        data.forEach(user => {
            statsList.innerHTML += `
                <div class="user-item">
                    <img src="${user.img}" alt="${user.name}">
                    <div class="user-details">
                        <span class="u-name">${user.name}</span>
                        <span class="u-username">@${user.username}</span>
                    </div>
                    <button class="btn-follow-mini">S'abonner</button>
                </div>
            `;
        });
        
        statsModal.style.display = 'flex';
    }

    // Événements de clic
    document.getElementById('open-followers').onclick = () => showStats('followers');
    document.getElementById('open-following').onclick = () => showStats('following');
    closeStats.onclick = () => statsModal.style.display = 'none';

    // Fermer si on clique à côté
    window.onclick = (e) => {
        if (e.target === statsModal) statsModal.style.display = 'none';
    };
});



// menu HTML

document.addEventListener('DOMContentLoaded', () => {
    const tabs = document.querySelectorAll('.tab-btn');
    const displayContainer = document.getElementById('settings-display');
    const panes = document.querySelectorAll('.content-pane');
    const mobileBackBtn = document.getElementById('mobile-back-btn');

    // 1. Gestion des clics sur le menu
    tabs.forEach(tab => {
        tab.addEventListener('click', () => {
            // Activer le panneau central
            displayContainer.classList.add('visible');

            // Gérer les états des boutons (Accessibilité)
            tabs.forEach(t => {
                t.classList.remove('active');
                t.setAttribute('aria-selected', 'false');
            });
            tab.classList.add('active');
            tab.setAttribute('aria-selected', 'true');

            // Afficher le bon contenu
            const target = tab.getAttribute('data-target');
            panes.forEach(pane => {
                pane.classList.remove('active');
                if (pane.id === target) {
                    pane.classList.add('active');
                }
            });
        });
    });

    // 2. Gestion du bouton retour sur Mobile
    if (mobileBackBtn) {
        mobileBackBtn.addEventListener('click', () => {
            // Masque le panneau central pour révéler à nouveau le menu
            displayContainer.classList.remove('visible');
            
            // Réinitialise les boutons
            tabs.forEach(t => {
                t.classList.remove('active');
                t.setAttribute('aria-selected', 'false');
            });
        });
    }
});



// Aperçu de la photo de profil
const imageUpload = document.getElementById('imageUpload');
const imagePreview = document.getElementById('imagePreview');

if (imageUpload) {
    imageUpload.addEventListener('change', function() {
        const file = this.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onload = function(e) {
                imagePreview.setAttribute('src', e.target.result);
            }
            reader.readAsDataURL(file);
        }
    });
}


document.addEventListener('DOMContentLoaded', () => {
    const tabs = document.querySelectorAll('.tab-btn');
    const panes = document.querySelectorAll('.content-pane');
    const display = document.getElementById('settings-display');
    const mobileBackBtn = document.getElementById('mobile-back-btn');

    tabs.forEach(tab => {
        tab.addEventListener('click', () => {
            const target = tab.getAttribute('data-target');

            // 1. Gérer l'état actif des boutons
            tabs.forEach(t => t.classList.remove('active'));
            tab.classList.add('active');

            // 2. Changer le contenu à droite
            panes.forEach(pane => {
                pane.classList.remove('active');
                if (pane.id === target) pane.classList.add('active');
            });

            // 3. Sur mobile, faire glisser le panneau vers l'avant
            if (window.innerWidth <= 800) {
                display.classList.add('visible');
            }
        });
    });

    // Bouton retour mobile
    mobileBackBtn.addEventListener('click', () => {
        display.classList.remove('visible');
    });
});



document.addEventListener('DOMContentLoaded', () => {
    // 1. GESTION DES ONGLETS
    const tabs = document.querySelectorAll('.profile-tabs .tab');
    const contents = document.querySelectorAll('.tab-content');

    tabs.forEach(tab => {
        tab.addEventListener('click', (e) => {
            e.preventDefault();
            // Retirer l'état actif partout
            tabs.forEach(t => t.classList.remove('active'));
            contents.forEach(c => c.classList.remove('active'));

            // Ajouter l'état actif sur l'élément cliqué
            tab.classList.add('active');
            const targetId = tab.getAttribute('href').substring(1);
            document.getElementById(targetId).classList.add('active');
        });
    });

    // 2. GESTION DES MODALES
    const editModal = document.getElementById('edit-modal');
    const statsModal = document.getElementById('stats-modal');

    // Ouverture Edition
    const openEditDesktop = document.getElementById('open-edit');
    const openEditMobile = document.getElementById('open-edit-mobile');
    const openEdit = () => { editModal.style.display = 'flex'; };
    if(openEditDesktop) openEditDesktop.addEventListener('click', openEdit);
    if(openEditMobile) openEditMobile.addEventListener('click', openEdit);

    // Ouverture Stats
    document.getElementById('open-followers').addEventListener('click', () => { statsModal.style.display = 'flex'; });
    document.getElementById('open-following').addEventListener('click', () => { statsModal.style.display = 'flex'; });

    // Fermeture des modales
    document.querySelectorAll('.close-btn').forEach(btn => {
        btn.addEventListener('click', function() {
            this.closest('.modal-overlay').style.display = 'none';
        });
    });

    // Fermeture au clic à l'extérieur
    window.addEventListener('click', (e) => {
        if (e.target.classList.contains('modal-overlay')) {
            e.target.style.display = 'none';
        }
    });
});



/* ============================================================
   ACTION BOUTON POUR PARTAGER LE PROFIL (PC & Mobile)
   ============================================================ */
document.addEventListener('DOMContentLoaded', () => {
    // On sélectionne les deux boutons (celui du PC et celui du Mobile)
    const shareBtns = document.querySelectorAll('#btn btn-secondary, #share-profile-btn-mobile');

    shareBtns.forEach(btn => {
        btn.addEventListener('click', async () => {
            const shareData = {
                title: 'Tynorah',
                text: 'Découvre mon profil sur Tynorah !',
                url: window.location.href // Partage l'URL actuelle
            };

            try {
                // Vérifie si le navigateur supporte le partage natif (Téléphone)
                if (navigator.share) {
                    await navigator.share(shareData);
                    console.log('Profil partagé avec succès');
                } else {
                    // Alternative pour PC : Copier le lien
                    await navigator.clipboard.writeText(window.location.href);
                    alert('Lien du profil copié dans le presse-papier !');
                }
            } catch (err) {
                console.log('Erreur lors du partage :', err);
            }
        });
    });
});
document.addEventListener('DOMContentLoaded', () => {
  const tabBtns = document.querySelectorAll('.tab-btn');
  const tabContents = document.querySelectorAll('.tab-content');

  tabBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      // 1. Retirer la classe 'active' de tous les boutons et contenus
      tabBtns.forEach(b => b.classList.remove('active'));
      tabContents.forEach(c => c.classList.remove('active'));

      // 2. Ajouter la classe 'active' au bouton cliqué
      btn.classList.add('active');

      // 3. Afficher le contenu correspondant
      const targetId = btn.getAttribute('data-target');
      document.getElementById(targetId).classList.add('active');
    });
  });
});



document.addEventListener('DOMContentLoaded', () => {
    const tabs = document.querySelectorAll(".tab");
    const contents = document.querySelectorAll(".tab-content");

    tabs.forEach(tab => {
        tab.addEventListener("click", function(e) {
            e.preventDefault();
            
            // On retire l'état actif partout
            tabs.forEach(t => t.classList.remove("active"));
            contents.forEach(c => c.classList.remove("active"));

            // On active l'onglet cliqué
            this.classList.add("active");

            // On affiche le contenu lié à l'ID (ex: #tab-publications)
            const targetId = this.getAttribute("href");
            const target = document.querySelector(targetId);
            if (target) target.classList.add("active");
        });
    });
});


/* ============================================================
   MESSAGERIE (Ouverture / Fermeture du Chat sur Mobile)
   ============================================================ */
function openMobileChat() {
    const chatWindow = document.getElementById('chat-window');
    // Sur mobile (largeur < 768px), on fait glisser la fenêtre
    if (window.innerWidth <= 768 && chatWindow) {
        chatWindow.classList.add('active');
    }
}

function closeMobileChat() {
    const chatWindow = document.getElementById('chat-window');
    if (chatWindow) {
        chatWindow.classList.remove('active');
    }
}



import { getAuth, signInWithEmailAndPassword } from "firebase/auth";

const auth = getAuth();
const btnLogin = document.getElementById('login-btn');

btnLogin.addEventListener('click', () => {
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    // Firebase vérifie si le compte existe
    signInWithEmailAndPassword(auth, email, password)
      .then((userCredential) => {
        // Connecté avec succès ! On redirige vers le Feed.
        window.location.href = "feed.html";
      })
      .catch((error) => {
        alert("Mauvais mot de passe ou email !");
      });
});




import { getFirestore, collection, addDoc, onSnapshot } from "firebase/firestore"; 

const db = getFirestore();

// 1. ENVOYER UN MESSAGE DANS LA BASE DE DONNÉES
function envoyerMessage(texte) {
  addDoc(collection(db, "messages"), {
    texte: texte,
    auteur: "Maelo",
    heure: new Date()
  });
}

// 2. ÉCOUTER LA BASE DE DONNÉES EN TEMPS RÉEL (La Magie !)
// Dès qu'un nouveau message arrive dans la base, cette fonction s'active automatiquement
onSnapshot(collection(db, "messages"), (snapshot) => {
    snapshot.docChanges().forEach((change) => {
        if (change.type === "added") {
            const data = change.doc.data();
            // On affiche la bulle sur l'écran
            ajouterBulle(data.texte); 
        }
    });
});




/* ============================================================
   GESTION DE LA CONNEXION (index.html / signin)
   ============================================================ */
const loginForm = document.getElementById('login-form');

if (loginForm) {
    // Si tu as un div pour les erreurs, sinon on utilisera alert()
    // const errorDiv = document.getElementById('error-message'); 

    loginForm.addEventListener('submit', (e) => {
        e.preventDefault();

        const email = document.getElementById('login-email').value.trim();
        const password = document.getElementById('login-password').value;
        const btn = loginForm.querySelector('button[type="submit"]');

        btn.textContent = "Connexion...";
        btn.disabled = true;

        // APPEL À FIREBASE POUR VÉRIFIER LE COMPTE
        signInWithEmailAndPassword(auth, email, password)
            .then((userCredential) => {
                // Connexion réussie !
                const user = userCredential.user;
                console.log("Connecté :", user.email);
                
                // Redirection vers le fil d'actualité
                window.location.href = "feed.html";
            })
            .catch((error) => {
                // Mot de passe faux, ou compte inexistant
                btn.textContent = "SIGN IN";
                btn.disabled = false;
                
                // Tu peux afficher l'erreur proprement si tu as un <div> prévu pour
                alert("Identifiants incorrects. Veuillez réessayer.");
                console.error(error.code, error.message);
            });
    });
}