"use client";

import React, { useEffect, useRef, useState } from "react";

interface HorseProps {
  interactive?: boolean;
}

export const AnimatedHorse: React.FC<HorseProps> = ({ interactive = true }) => {
  const canvasRef = useRef<HTMLCanvasElement | null>(null);
  const [isPlaying, setIsPlaying] = useState<boolean>(true);
  const [activeTier, setActiveTier] = useState<string>("Local Ollama (Emerald)");

  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;
    const ctx = canvas.getContext("2d");
    if (!ctx) return;

    let animId: number;
    let t = 0;

    // Check prefers-reduced-motion
    const mediaQuery = window.matchMedia("(prefers-reduced-motion: reduce)");
    if (mediaQuery.matches) {
      setIsPlaying(false);
    }

    const resize = () => {
      const rect = canvas.getBoundingClientRect();
      canvas.width = rect.width * (window.devicePixelRatio || 1);
      canvas.height = rect.height * (window.devicePixelRatio || 1);
    };
    resize();
    window.addEventListener("resize", resize);

    const render = () => {
      if (!ctx || !canvas) return;
      const dpr = window.devicePixelRatio || 1;
      const width = canvas.width / dpr;
      const height = canvas.height / dpr;

      ctx.save();
      ctx.scale(dpr, dpr);
      ctx.clearRect(0, 0, width, height);

      const cx = width / 2;
      const cy = height / 2 + 30;

      if (isPlaying) {
        t += 0.04;
      }

      // Breathing bob & trot cycle
      const bob = Math.sin(t * 2) * 6;
      const trot = Math.sin(t * 3);

      // Cybernetic ground grid
      ctx.strokeStyle = "rgba(37, 99, 235, 0.12)";
      ctx.lineWidth = 1;
      for (let i = -6; i <= 6; i++) {
        const gx = cx + i * 40;
        ctx.beginPath();
        ctx.moveTo(gx - 40, cy + 90);
        ctx.lineTo(gx + 60, cy + 140);
        ctx.stroke();
      }

      // Shadow
      ctx.fillStyle = "rgba(0, 0, 0, 0.4)";
      ctx.beginPath();
      ctx.ellipse(cx, cy + 95, 90 + trot * 8, 16, 0, 0, Math.PI * 2);
      ctx.fill();

      // Back legs
      ctx.strokeStyle = "#1e293b";
      ctx.lineWidth = 8;
      ctx.lineCap = "round";

      // Back-left leg
      ctx.beginPath();
      ctx.moveTo(cx - 50, cy + 10 + bob);
      ctx.lineTo(cx - 65 - Math.sin(t * 3) * 15, cy + 55);
      ctx.lineTo(cx - 70 - Math.sin(t * 3) * 20, cy + 90);
      ctx.stroke();

      // Back-right leg
      ctx.beginPath();
      ctx.moveTo(cx + 45, cy + 10 + bob);
      ctx.lineTo(cx + 35 + Math.sin(t * 3) * 15, cy + 55);
      ctx.lineTo(cx + 30 + Math.sin(t * 3) * 20, cy + 90);
      ctx.stroke();

      // Main Torso Chassis (Faceted Titanium)
      ctx.fillStyle = "#141619";
      ctx.strokeStyle = "#2563EB";
      ctx.lineWidth = 2;
      ctx.beginPath();
      ctx.moveTo(cx - 70, cy + bob - 15);
      ctx.lineTo(cx + 50, cy + bob - 25);
      ctx.lineTo(cx + 70, cy + bob + 10);
      ctx.lineTo(cx - 40, cy + bob + 30);
      ctx.lineTo(cx - 80, cy + bob + 10);
      ctx.closePath();
      ctx.fill();
      ctx.stroke();

      // Front legs
      ctx.strokeStyle = "#334155";
      ctx.lineWidth = 9;

      // Front-left leg
      ctx.beginPath();
      ctx.moveTo(cx - 40, cy + 20 + bob);
      ctx.lineTo(cx - 35 + Math.sin(t * 3) * 18, cy + 60);
      ctx.lineTo(cx - 30 + Math.sin(t * 3) * 24, cy + 92);
      ctx.stroke();

      // Front-right leg
      ctx.beginPath();
      ctx.moveTo(cx + 50, cy + 20 + bob);
      ctx.lineTo(cx + 60 - Math.sin(t * 3) * 18, cy + 60);
      ctx.lineTo(cx + 65 - Math.sin(t * 3) * 24, cy + 92);
      ctx.stroke();

      // Neck
      ctx.fillStyle = "#1e2328";
      ctx.beginPath();
      ctx.moveTo(cx + 35, cy + bob - 20);
      ctx.lineTo(cx + 75, cy + bob - 75);
      ctx.lineTo(cx + 95, cy + bob - 60);
      ctx.lineTo(cx + 60, cy + bob - 5);
      ctx.closePath();
      ctx.fill();
      ctx.stroke();

      // Cybernetic Head
      ctx.fillStyle = "#141619";
      ctx.beginPath();
      ctx.moveTo(cx + 70, cy + bob - 80);
      ctx.lineTo(cx + 115, cy + bob - 70);
      ctx.lineTo(cx + 125, cy + bob - 55);
      ctx.lineTo(cx + 85, cy + bob - 45);
      ctx.closePath();
      ctx.fill();
      ctx.stroke();

      // Optic sensor (Eyes)
      ctx.fillStyle = "#FFB000";
      ctx.shadowColor = "#FFB000";
      ctx.shadowBlur = 12;
      ctx.beginPath();
      ctx.arc(cx + 100, cy + bob - 65, 3.5, 0, Math.PI * 2);
      ctx.fill();
      ctx.shadowBlur = 0;

      // Fiber-optic mane
      ctx.strokeStyle = "#FFB000";
      ctx.lineWidth = 2;
      for (let m = 0; m < 5; m++) {
        const mx = cx + 45 + m * 9;
        const my = cy + bob - 30 - m * 9;
        ctx.beginPath();
        ctx.moveTo(mx, my);
        ctx.quadraticCurveTo(
          mx - 20 + Math.sin(t * 2 + m) * 6,
          my - 15,
          mx - 35,
          my + 5
        );
        ctx.stroke();
      }

      // 5-Cycle Glowing Neural Core
      const corePulse = Math.sin(t * 4);
      const coreRadius = 14 + corePulse * 3;
      const coreX = cx + 10;
      const coreY = cy + bob + 5;

      const gradient = ctx.createRadialGradient(coreX, coreY, 2, coreX, coreY, coreRadius * 2);
      gradient.addColorStop(0, "rgba(16, 185, 129, 0.95)");
      gradient.addColorStop(0.5, "rgba(37, 99, 235, 0.5)");
      gradient.addColorStop(1, "rgba(16, 185, 129, 0)");

      ctx.fillStyle = gradient;
      ctx.beginPath();
      ctx.arc(coreX, coreY, coreRadius * 2, 0, Math.PI * 2);
      ctx.fill();

      // Core Crystal Octahedron
      ctx.strokeStyle = "#10B981";
      ctx.lineWidth = 2.5;
      ctx.shadowColor = "#10B981";
      ctx.shadowBlur = 14;
      ctx.beginPath();
      ctx.moveTo(coreX, coreY - 12);
      ctx.lineTo(coreX + 10, coreY);
      ctx.lineTo(coreX, coreY + 12);
      ctx.lineTo(coreX - 10, coreY);
      ctx.closePath();
      ctx.stroke();
      ctx.shadowBlur = 0;

      ctx.restore();
      animId = requestAnimationFrame(render);
    };

    render();

    return () => {
      cancelAnimationFrame(animId);
      window.removeEventListener("resize", resize);
    };
  }, [isPlaying]);

  return (
    <div className="relative w-full h-[400px] flex items-center justify-center overflow-hidden rounded-2xl border border-[var(--border-color)] bg-[var(--bg-surface)]">
      <canvas ref={canvasRef} className="w-full h-full cursor-pointer" />

      {/* WCAG 2.2.2 Accessible Pause/Play Control */}
      <button
        onClick={() => setIsPlaying((p) => !p)}
        type="button"
        className="absolute bottom-4 left-4 z-20 px-3.5 py-1.5 text-xs font-mono font-semibold uppercase tracking-wider rounded-lg border border-[var(--border-color)] bg-[var(--bg-primary)] hover:bg-[var(--bg-surface-elevated)] text-[var(--text-primary)] transition-colors shadow-md"
      >
        {isPlaying ? "⏸ Pause Mascot" : "▶ Play Mascot"}
      </button>

      {/* Active Neural Core Tier Badge */}
      <div className="absolute top-4 right-4 z-20 px-3 py-1.5 text-xs font-mono rounded-full border border-emerald-500/40 bg-emerald-950/60 text-emerald-300 flex items-center gap-2 backdrop-blur-md">
        <span className="w-2 h-2 rounded-full bg-emerald-400 animate-pulse" />
        <span>5-Cycle Neural Core: Active</span>
      </div>
    </div>
  );
};
