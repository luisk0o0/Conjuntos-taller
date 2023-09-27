```mermaid
stateDiagram
    [*] --> Reservado: Usuario reserva turno
    Reservado --> Confirmado: Administrador confirma reserva
    Reservado --> Cancelado: Usuario cancela reserva
    Confirmado --> Completado: Turno ha pasado y se completa
    Reservado --> Cancelado: Usuario cancela reserva
    Cancelado --> [*]: Reserva cancelada
    Confirmado --> [*]: Turno completado
    Cancelado --> [*]: Reserva cancelada
    Completado --> [*]: Turno completado
    state Reservado {
        [*] --> Reservado: Usuario reserva turno
        Reservado --> Confirmado: Administrador confirma reserva
        Reservado --> Cancelado: Usuario cancela reserva
    }
    state Confirmado {
        Confirmado --> Completado: Turno ha pasado y se completa
        Confirmado --> [*]: Turno completado
    }
    state Cancelado {
        Cancelado --> [*]: Reserva cancelada
    }
    state Completado {
        Completado --> [*]: Turno completado
    }
