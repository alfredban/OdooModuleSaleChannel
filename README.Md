# 🧾 Trabajo Práctico – Gestión de Canales de Venta en Odoo

## 📋 Descripción General

Este módulo de Odoo permite gestionar **canales de venta** para la empresa **XXXXX**, con el objetivo de **controlar las ventas realizadas**, **las entregas de productos** y **las facturas asociadas a dichas ventas**.  

Cada canal de venta define un **almacén de entrega** y un **diario de facturación**, que se aplican automáticamente en las órdenes de venta, entregas y facturas generadas.

---

## ⚙️ Funcionalidades Implementadas

### 1. Gestión de Canales de Venta

Se incorporó un nuevo modelo de **Canales de Venta**, accesible desde el menú:

> **Ventas → Configuración → Canales de Venta**

Cada canal incluye los siguientes campos:

| Campo | Descripción | Tipo | Requerido |
|--------|--------------|------|------------|
| **Nombre** | Nombre identificativo del canal. | `Char` | ✅ |
| **Código** | Código único del canal. | `Char` | ✅ |
| **Depósito (Almacén)** | Almacén desde donde se despacha la mercadería. | `Many2one` (`stock.warehouse`) | ❌ |
| **Diario de Facturación** | Diario contable utilizado para la emisión de facturas. | `Many2one` (`account.journal`) | ❌ |

---

### 2. Adaptaciones en la Orden de Venta

Se realizaron modificaciones sobre el modelo **`sale.order`** para integrar la funcionalidad de los canales de venta.

#### a. Selección del Canal de Venta

- Se agregó el campo **`canal_id`**, obligatorio en la orden.
- El usuario debe seleccionar un canal antes de confirmar la venta.

#### b. Almacén de Entrega Automático

- Al seleccionar un canal, el **almacén de entrega** de la orden se actualiza automáticamente de acuerdo al depósito configurado en el canal.
- Las **órdenes de entrega (`stock.picking`)** generadas desde la orden utilizan ese mismo almacén.

#### c. Diario de Facturación Asociado

- Las **facturas emitidas** desde la orden de venta utilizan el **diario contable** definido en el canal correspondiente.
- Se garantiza coherencia entre la venta, el canal y el diario asignado.

#### d. Propagación del Canal

- El **canal de venta** se traslada automáticamente a:
  - Las **órdenes de entrega (`stock.picking`)**
  - Las **facturas (`account.move`)**

Esto permite **filtrar y agrupar** órdenes de venta, entregas y facturas por canal desde las vistas de Odoo.

---

## 🧠 Aspectos Técnicos Relevantes

- Se utilizaron **campos `onchange`** para actualizar dinámicamente el depósito y el diario según el canal seleccionado.  
- Se empleó **herencia de modelos (`_inherit`)** sobre `sale.order`, `stock.picking` y `account.move` para propagar el canal de venta.  
- Se agregaron las vistas necesarias para incluir el campo de canal en los formularios de venta, entrega y facturación.  

---

## 🧾 Ejemplo de Flujo

1. Crear un canal de venta **“Online”** con:  
   - Código: `ONL`  
   - Depósito: “Almacén Principal”  
   - Diario: “Ventas Online”  

2. Crear una **orden de venta** y seleccionar el canal **Online**.  
3. Al confirmar la orden:  
   - Se asigna el depósito “Almacén Principal”.  
   - Se genera una entrega desde ese depósito.  
   - La factura se emite con el diario “Ventas Online”.  
   - El canal se replica en todos los documentos relacionados.

---

## 🧑‍💻 Instalación

1. Copiar el módulo en la carpeta de **addons personalizados**.  
2. Actualizar la lista de módulos desde el backend de Odoo.  
3. Instalar el módulo **Gestión de Canales de Venta**.  
4. Configurar los canales desde:  
   > **Ventas → Configuración → Canales de Venta**

---

## 👥 Autores (GRUPO A)

- **Ferreiro, Ramiro Xavier**
- **Guerrero, Manuel Florian**  
- **Ivanovich, Alfredo Honorio**   


