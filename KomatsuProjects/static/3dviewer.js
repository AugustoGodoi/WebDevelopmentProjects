// Configuração básica da cena, câmera e renderizador
const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
const renderer = new THREE.WebGLRenderer();

renderer.setSize(window.innerWidth, window.innerHeight);
document.body.appendChild(renderer.domElement);

// Carregar o modelo .obj
const loader = new THREE.OBJLoader();
loader.load(
    './3dfiles/3d.obj',
    function (object) {
        scene.add(object);
    },
    function (xhr) {
        console.log((xhr.loaded / xhr.total * 100) + '% carregado');
    },
    function (error) {
        console.error('Erro ao carregar o modelo', error);
    }
);

// Configuração da câmera e controle da visualização
camera.position.z = 5;

const ambientLight = new THREE.AmbientLight(0xffffff, 0.5); // Cor e intensidade da luz ambiente
scene.add(ambientLight);


// Função para renderizar a cena
function animate() {
    requestAnimationFrame(animate);
    renderer.render(scene, camera);
}

// Iniciar a animação/renderização
animate();
