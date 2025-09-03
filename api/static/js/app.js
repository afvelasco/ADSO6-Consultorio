const API_URL = 'http://localhost:8001/especialistas';

// DOM Elements
const form = document.getElementById('especialistaForm');
const cancelEditBtn = document.getElementById('cancelEdit');
const tableBody = document.getElementById('especialistasTable');
const formTitle = document.getElementById('form-title');

// Estado para controlar si estamos editando
let isEditing = false;
let currentEditId = null;

// Cargar especialistas al iniciar
document.addEventListener('DOMContentLoaded', loadEspecialistas);

// Manejar envío del formulario
form.addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const especialista = {
        id: document.getElementById('especialistaId').value || null,
        nombre: document.getElementById('nombre').value,
        especialidad: document.getElementById('especialidad').value,
        foto: document.getElementById('foto').value || 'https://via.placeholder.com/100'
    };

    if (isEditing) {
        await updateEspecialista(currentEditId, especialista);
    } else {
        await createEspecialista(especialista);
    }
    
    resetForm();
    loadEspecialistas();
});

// Cancelar edición
cancelEditBtn.addEventListener('click', resetForm);

// Función para cargar todos los especialistas
async function loadEspecialistas() {
    try {
        const response = await fetch(API_URL);
        const data = await response.json();
        
        tableBody.innerHTML = '';
        
        data.especialistas.forEach(esp => {
            const row = document.createElement('tr');
            row.innerHTML = `
                <td><img src="${esp.foto}" alt="${esp.nombre}" class="especialista-img"></td>
                <td>${esp.id}</td>
                <td>${esp.nombre}</td>
                <td>${esp.especialidad}</td>
                <td class="action-buttons">
                    <button class="btn btn-sm btn-warning" onclick="editEspecialista(${esp.id})">Editar</button>
                    <button class="btn btn-sm btn-danger" onclick="deleteEspecialista(${esp.id})">Eliminar</button>
                </td>
            `;
            tableBody.appendChild(row);
        });
    } catch (error) {
        console.error('Error al cargar especialistas:', error);
        alert('Error al cargar los especialistas');
    }
}

// Función para crear un nuevo especialista
async function createEspecialista(especialista) {
    try {
        const response = await fetch(API_URL, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(especialista)
        });
        
        const result = await response.json();
        alert(result.mensaje);
    } catch (error) {
        console.error('Error al crear especialista:', error);
        alert('Error al crear el especialista');
    }
}

// Función para cargar datos de un especialista para editar
async function editEspecialista(id) {
    try {
        const response = await fetch(`${API_URL}/${id}`);
        const especialista = await response.json();
        
        if (especialista.mensaje) {
            alert(especialista.mensaje);
            return;
        }
        
        // Llenar el formulario con los datos
        document.getElementById('especialistaId').value = especialista.id;
        document.getElementById('nombre').value = especialista.nombre;
        document.getElementById('especialidad').value = especialista.especialidad;
        document.getElementById('foto').value = especialista.foto;
        
        // Cambiar a modo edición
        isEditing = true;
        currentEditId = id;
        formTitle.textContent = 'Editar Especialista';
        cancelEditBtn.style.display = 'inline-block';
        
        // Scroll al formulario
        form.scrollIntoView({ behavior: 'smooth' });
    } catch (error) {
        console.error('Error al cargar especialista:', error);
        alert('Error al cargar el especialista para editar');
    }
}

// Función para actualizar un especialista
async function updateEspecialista(id, especialista) {
    try {
        const response = await fetch(`${API_URL}/${id}`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(especialista)
        });
        
        const result = await response.json();
        alert(result.mensaje);
    } catch (error) {
        console.error('Error al actualizar especialista:', error);
        alert('Error al actualizar el especialista');
    }
}

// Función para eliminar un especialista
async function deleteEspecialista(id) {
    if (!confirm('¿Estás seguro de que quieres eliminar este especialista?')) {
        return;
    }
    
    try {
        const response = await fetch(`${API_URL}/${id}`, {
            method: 'DELETE'
        });
        
        const result = await response.json();
        alert(result.mensaje);
        loadEspecialistas();
    } catch (error) {
        console.error('Error al eliminar especialista:', error);
        alert('Error al eliminar el especialista');
    }
}

// Función para resetear el formulario
function resetForm() {
    form.reset();
    document.getElementById('especialistaId').value = '';
    isEditing = false;
    currentEditId = null;
    formTitle.textContent = 'Agregar Nuevo Especialista';
    cancelEditBtn.style.display = 'none';
}