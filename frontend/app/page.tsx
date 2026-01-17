import Image from "next/image";
import ChatWidget from "../components/ChatWidget";

export default function Home() {
  return (
    <div className="min-h-screen bg-slate-50 font-sans text-slate-900">
      {/* Navigation */}
      <nav className="sticky top-0 z-40 w-full bg-white/80 backdrop-blur-md border-b border-gray-100">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex justify-between h-16 items-center">
            <div className="flex items-center gap-2">
              <div className="w-8 h-8 bg-blue-600 rounded-lg flex items-center justify-center text-white font-bold">
                G
              </div>
              <span className="font-bold text-xl tracking-tight text-slate-800">GiftsCorp</span>
            </div>
            <div className="hidden md:flex items-center space-x-8 text-sm font-medium text-slate-600">
              <a href="#" className="hover:text-blue-600 transition">Collections</a>
              <a href="#" className="hover:text-blue-600 transition">Customization</a>
              <a href="#" className="hover:text-blue-600 transition">About Us</a>
              <a href="#" className="px-4 py-2 bg-slate-900 text-white rounded-full hover:bg-slate-800 transition">
                Contact Sales
              </a>
            </div>
          </div>
        </div>
      </nav>

      {/* Hero Section */}
      <section className="relative pt-20 pb-32 overflow-hidden">
        <div className="absolute inset-0 bg-blue-50 -z-10">
          <div className="absolute top-0 right-0 w-1/2 h-full bg-gradient-to-l from-blue-100/50 to-transparent"></div>
        </div>
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center md:text-left flex flex-col md:flex-row items-center">
          <div className="md:w-1/2 space-y-6">
            <h1 className="text-4xl md:text-6xl font-extrabold tracking-tight text-slate-900 leading-tight">
              Corporate Gifting, <br />
              <span className="text-blue-600">Reimagined.</span>
            </h1>
            <p className="text-lg text-slate-600 max-w-lg mx-auto md:mx-0">
              Premium merchandise and custom souvenirs for your brand.
              Smart pricing, endless variety, and seamless ordering driven by AI.
            </p>
            <div className="flex flex-col sm:flex-row gap-4 justify-center md:justify-start">
              <button className="px-8 py-4 bg-blue-600 text-white font-semibold rounded-xl hover:bg-blue-700 shadow-lg shadow-blue-600/20 transition transform hover:-translate-y-1">
                Explore Catalog
              </button>
              <button className="px-8 py-4 bg-white text-slate-700 font-semibold rounded-xl border border-gray-200 hover:bg-gray-50 transition">
                View Case Studies
              </button>
            </div>
          </div>
          <div className="md:w-1/2 mt-12 md:mt-0 relative">
            <div className="relative w-full h-[400px] bg-gradient-to-tr from-blue-200 to-indigo-100 rounded-3xl overflow-hidden shadow-2xl">
              <div className="absolute inset-0 flex items-center justify-center text-blue-900/20 font-bold text-9xl select-none">
                G
              </div>
              {/* Decorative circles */}
              <div className="absolute top-10 right-10 w-20 h-20 bg-white/30 rounded-full blur-xl"></div>
              <div className="absolute bottom-10 left-10 w-32 h-32 bg-indigo-500/10 rounded-full blur-xl"></div>
            </div>
          </div>
        </div>
      </section>

      {/* Features Grid */}
      <section className="py-24 bg-white">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-16">
            <h2 className="text-3xl font-bold text-slate-900">Why Choose Us</h2>
            <p className="mt-4 text-slate-600">Experience the difference of data-driven merchandising.</p>
          </div>
          <div className="grid md:grid-cols-3 gap-8">
            {[
              { title: "Premium Quality", desc: "Curated materials that reflect your brand's excellence." },
              { title: "Smart Bundling", desc: "AI-powered recommendations to fit your exact budget." },
              { title: "Global Sourcing", desc: "Access to thousands of unique items from worldwide markets." }
            ].map((item, i) => (
              <div key={i} className="p-8 bg-slate-50 rounded-2xl border border-slate-100 hover:shadow-xl transition duration-300">
                <div className="w-12 h-12 bg-blue-100 rounded-xl mb-6 flex items-center justify-center text-blue-600 font-bold text-xl">
                  {i + 1}
                </div>
                <h3 className="text-xl font-bold mb-3">{item.title}</h3>
                <p className="text-slate-600">{item.desc}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Product Teaser */}
      <section className="py-24 bg-slate-50">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex justify-between items-end mb-12">
            <div>
              <h2 className="text-3xl font-bold text-slate-900">Featured Collections</h2>
              <p className="mt-2 text-slate-600">Best selling items this month.</p>
            </div>
            <a href="#" className="text-blue-600 font-medium hover:underline">View All &rarr;</a>
          </div>

          <div className="grid grid-cols-2 md:grid-cols-4 gap-6">
            {[1, 2, 3, 4].map((n) => (
              <div key={n} className="group bg-white rounded-2xl p-4 transition hover:shadow-lg border border-gray-100">
                <div className="aspect-square bg-gray-100 rounded-xl mb-4 relative overflow-hidden">
                  <div className="absolute inset-0 bg-gray-200 animate-pulse group-hover:bg-gray-300 transition"></div>
                </div>
                <h4 className="font-semibold text-slate-900">Premium Item {n}</h4>
                <p className="text-sm text-slate-500">Electronics</p>
                <div className="mt-2 flex justify-between items-center">
                  <span className="font-bold text-blue-600">$45.00</span>
                  <button className="w-8 h-8 rounded-full bg-gray-100 flex items-center justify-center hover:bg-blue-600 hover:text-white transition">
                    +
                  </button>
                </div>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Footer */}
      <footer className="bg-slate-900 text-slate-300 py-12">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 grid md:grid-cols-4 gap-8">
          <div>
            <div className="flex items-center gap-2 mb-4 text-white">
              <span className="font-bold text-xl">GiftsCorp</span>
            </div>
            <p className="text-sm text-slate-400">
              Elevating corporate relationships through thoughtful gifting.
            </p>
          </div>
          <div>
            <h4 className="font-bold text-white mb-4">Product</h4>
            <ul className="space-y-2 text-sm">
              <li><a href="#" className="hover:text-white">New Arrivals</a></li>
              <li><a href="#" className="hover:text-white">Best Sellers</a></li>
              <li><a href="#" className="hover:text-white">Bundles</a></li>
            </ul>
          </div>
          <div>
            <h4 className="font-bold text-white mb-4">Company</h4>
            <ul className="space-y-2 text-sm">
              <li><a href="#" className="hover:text-white">About</a></li>
              <li><a href="#" className="hover:text-white">Careers</a></li>
              <li><a href="#" className="hover:text-white">Contact</a></li>
            </ul>
          </div>
          <div>
            <h4 className="font-bold text-white mb-4">Legal</h4>
            <ul className="space-y-2 text-sm">
              <li><a href="#" className="hover:text-white">Privacy</a></li>
              <li><a href="#" className="hover:text-white">Terms</a></li>
            </ul>
          </div>
        </div>
      </footer>

      {/* Floating Chat Widget */}
      <ChatWidget />
    </div>
  );
}
