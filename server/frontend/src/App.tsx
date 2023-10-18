/**
 * Internal dependencies
 */
import { useEffect, useState } from 'react'

/**
 * Style dependencies
 */
import './App.scss'

function App() {
	const [message, setMessage] = useState('' as string)

	useEffect(() => {
		const socket = new WebSocket('ws://localhost:1337')

		const handleIncomingMessage = (event: MessageEvent) => {
			const message = event.data
			setMessage(message)
		}

		socket.addEventListener('message', handleIncomingMessage)

		document.addEventListener('keypress', event => {
			//SHIFT + 2 for å resette serveren med socketen.
			if (event.key === '"' && event.shiftKey) {
				socket.send('reset')
				window.location.reload()
			}
		})

		return () => {
			socket.removeEventListener('message', handleIncomingMessage)
			socket.close()
		}
	}, [])

	return <main>Melding fra server: {message}</main>
}

export default App
