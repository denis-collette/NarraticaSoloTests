// frontend/src/components/NavBar.tsx
import Link from "next/link";
import { Avatar, AvatarFallback, AvatarImage } from "@/components/ui/avatar";
import Search from "@/components/audio/custom/Search"; 

export default function NavBar() {
    return (
        <nav className="p-2 bg-[#120e0c] text-white">
        <ul className="flex items-center gap-5">
            {/* Search Component - Consider adding a container div if layout adjustments are needed */}
            <li>
            <Search />
            </li>
            <li>
            <Link href="/">Accueil</Link>
            </li>
            <li>
            <Link href="/profil">Profil</Link>
            </li>
            <li>
            <Link href="/login">Connexion</Link>
            </li>
            <li>
            <Link href="/signup">Inscription</Link>
            </li>
            <li>
            <Link href="/bookView">Book View</Link>
            </li>
            <li>
            <Link href="/playerView">Player View</Link>
            </li>
            <li>
            <Avatar>
                <AvatarImage src="https://github.com/shadcn.png" alt="User Avatar" />
                <AvatarFallback>CN</AvatarFallback>
            </Avatar>
            </li>
        </ul>
        </nav>
    );
}
